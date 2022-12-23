import asyncio
import json
import os
from datetime import datetime
from pathlib import Path
from typing import List
import struct

import aiohttp
from bleak import BleakClient, BleakScanner
from dotenv import load_dotenv

DURATION_URL = "https://wakatime.com/api/v1/users/current/summaries"
interesting_unknown_characteristics = [
    "00000006-0000-3512-2118-0009af100700",
    "00000007-0000-3512-2118-0009af100700",
]
BATTERY_LEVEL_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
CURRENT_TIME_UUID = "00002a2b-0000-1000-8000-00805f9b34fb"


def get_creds(key: str, env_path: Path) -> str:
    load_dotenv(env_path)
    credential = os.environ.get(key, "")
    return credential


async def get_day_stats(api_key: str, url: str, date: str) -> List:
    print("Getting your day's wakatime stats")
    async with aiohttp.ClientSession() as session:
        url = f"{url}?api_key={api_key}&start={date}&end={date}"
        async with session.get(url) as response:
            stats = await response.json()
            return stats


async def get_device_info(address: str):
    """
    print("Scanning for devices ...")
    devices = await BleakScanner.discover()
    for device in devices:
        print(device)
    print("Connecting to device...")
    """
    async with BleakClient(address) as client:
        if not client.is_connected:
            raise Exception("Device not connected")
        """
        services = await client.get_services()
        print("Getting device services...")
        for service in services:
            print(f"{service.uuid}:{service.description}")
            characteristics = service.characteristics
            for char in characteristics:
                print(f"\t{char.uuid}:{char.description}:{char.properties}")
        """
        batterylevel_bytes = await client.read_gatt_char(BATTERY_LEVEL_UUID)
        currenttime_bytes = await client.read_gatt_char(CURRENT_TIME_UUID)
        date_time = struct.unpack("<hbbbbbbbbb", currenttime_bytes)
        battery_level = int.from_bytes(batterylevel_bytes, byteorder="big")
        print(
            f"Battery Level: {str(battery_level)}% current date and time: {date_time}"
        )
        print("And now some unknown data...")
        for unknown_chr in interesting_unknown_characteristics:
            data = await client.read_gatt_char(unknown_chr)
            print(f"{unknown_chr} : {data}")


async def main():
    env_path = Path.cwd() / ".env"
    api_key = get_creds(key="API_KEY", env_path=env_path)
    device_address = get_creds(key="DEVICE_ADDRESS", env_path=env_path)
    today = datetime.today().strftime("%Y-%m-%d")
    waka_stats = (await get_day_stats(api_key=api_key, url=DURATION_URL, date=today),)
    waka_stats = json.dumps(waka_stats, indent=4)
    print(waka_stats)
    device_info = (await get_device_info(device_address),)


if __name__ == "__main__":
    asyncio.run(main())
