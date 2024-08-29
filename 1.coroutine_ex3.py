import asyncio

async def fetch_data(id: int, delay:int):
    print(f"Fetching data id: {id}")
    await asyncio.sleep(delay)
    print(f"Fetched data id: {id}")
    return {"data": "some data", "id": id, }

async def main():
    print(f"Start of main coroutine.")
    task1 = fetch_data(1,2) 
    task2 = fetch_data(2,2)

    result1 = await task1
    print(f"Received result: {result1}")

    print()

    result2 = await task2
    print(f"Received result: {result2}")
    
# run the event loop 
asyncio.run(main())