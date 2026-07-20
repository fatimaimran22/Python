import asyncio

async def download_file(filename, seconds):
    if filename=="data.txt":
        raise Exception
    print(f"Starting download: {filename}")
    await asyncio.sleep(seconds)
    print(f"Finish Download: {filename} in {seconds} seconds")

    return str(filename) + "downloaded."

async def main():
    tasks=(
        download_file("data1.txt",2),
        download_file("data2.txt",3),
        download_file("data3.txt",1),
        download_file("data.txt",1))
    
    results=await asyncio.gather(*tasks, return_exceptions=True)    #donot raise exception

    for r in results:
        if isinstance(r,Exception):
            print("Download Failed")
        else:
            print("Download Successful.")
    
asyncio.run(main())


async def place_order(customer, prep_time):
    print(f"Customer {customer} order starts.")
    await asyncio.sleep(prep_time)
    print(f"Customer: {customer} order completed after {prep_time} seconds.")

    return f"{customer} order is ready!"


async def food_delivery():
    customers=(
        place_order("Fatima",2),
        place_order("Ali",1),
        place_order("Hajra",3),
        place_order("Abdul",0.5),
    )

    results=await asyncio.gather(*customers)

    for r in results:
        print(r)

asyncio.run(food_delivery())