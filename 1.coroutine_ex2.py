import asyncio

# define coroutine that simulates a time-consuming task
async def fetch_data(delay:int):
    print("Fetching data...")
    await asyncio.sleep(delay) # simulates I/O operation with a sleep
    print(f"Data Fetched")
    return {"data": "some data."} # return dict some data. 


#define another coroutine that calls the first coroutine
async def main():
    print(f"Start of main coroutine")
    task = fetch_data(2) # just create coroutine object not yet await it
    # await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task # coroutine start executed
    print(f"Recieved result: {result}")
    print(f"End of main coroutine.")
    

#Run the main coroutine
asyncio.run(main())