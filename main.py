import multiprocessing as mp
import os

def run_script(link):
    os.system(f"python view.py {link}")

if __name__ == "__main__":
    num_processes = int(input("Nhập số lượng tiến trình bạn muốn chạy đồng thời: "))
    link = input("Nhập link video TikTok: ")
    processes = []
    running = False

    while True:
        input("Nhấn Enter để bắt đầu/ tạm dừng chương trình")
        running = not running

        if running:
            print("Bắt đầu chạy tiến trình xem video.")
            for _ in range(num_processes):
                process = mp.Process(target=run_script, args=(link,))
                process.start()
                processes.append(process)
        else:
            print("Dừng chương trình...")
            for process in processes:
                if process.is_alive():
                    process.terminate()
            print("Chương trình đã dừng.")

            # Clear the processes list
            processes = []

        # Wait for all processes to terminate before asking for input again
        for process in processes:
            process.join()
