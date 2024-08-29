import asyncio

async def fetch_data(id: int, delay:int=2):
    print(f"Fetching data id: {id}")
    await asyncio.sleep(delay)
    print(f"Fetched data id: {id}")
    return {"data": "some data", "id": id, }

async def main():
    # Create task to run multiple coroutine currently
    task1 = asyncio.create_task(fetch_data(id=1))
    task2 = asyncio.create_task(fetch_data(id=2))
    task3 = asyncio.create_task(fetch_data(id=3))

    result1 = await task1
    result2 = await task2
    result3 = await task3
    