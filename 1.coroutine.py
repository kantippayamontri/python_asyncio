import asyncio

#coroutine function
async def main():
    print("Start of main coroutine")

# main() -> coroutine object
# main() # will return error cuz main() is a coroutine object need to await in order to get the result

# Run the main coroutine
asyncio.run(main()) #asyncio.run = run the event loop