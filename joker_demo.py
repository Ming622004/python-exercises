import requests
import subprocess


def movieffm(url_source, file_path, filename):
    # url_source = "https://baidu.com-ok-baidu.com/20191010/15278_dcf26eb0/1000k/hls/d7c48575927000000.ts"
    # url_source = input("input xhr_request_url:")
    # file_no = input("filename sr(01):")
    url = url_source[0:-8]
    print(url)
    no = ""
    # infile = ".Video" + file_no + ".ts"
    save_filename = file_path + filename + ".ts"
    with open(save_filename, "wb") as f:
        chuck_size = 1024

        for i in range(0, 1733):
            if(len(str(i))) == 1:
                no = "0000" + str(i)
            elif(len(str(i))) == 2:
                no = "000" + str(i)
            elif(len(str(i))) == 3:
                no = "00" + str(i)
            elif(len(str(i))) == 4:
                no = "0" + str(i)
            elif(len(str(i))) == 5:
                no = str(i)
            else:
                print("error")

            url_request = url + no + ".ts"
            print(url_request)

            r = requests.get(url_request, stream=True)
            for chunk in r.iter_content(chunk_size=chuck_size):
                f.write(chunk)

    print("ts download done!")


def ts2mp4(file_path, filename):
    ts_filename = file_path + filename + ".ts"
    mp4_filename = file_path + filename + ".mp4"
    subprocess.run(["D:/work_test/ffmpeg/bin/ffmpeg", "-i", ts_filename, mp4_filename])
    print("Transfer to mp4 done")


def main():
    url = "https://baidu.com-ok-baidu.com/20191010/15278_dcf26eb0/1000k/hls/d7c48575927000000.ts"
    file_path = "D:/work_test/"
    filename = "Joker"
    movieffm(url, file_path, filename)
    ts2mp4(file_path, filename)


if __name__ == '__main__':
    main()
