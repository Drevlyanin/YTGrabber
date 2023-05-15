from pytube import YouTube
from moviepy.editor import *

def download_youtube_video():
    url = input("Введите ссылку на YouTube видео: ")

    try:
        yt = YouTube(url)
        available_streams = yt.streams.filter(progressive=True).order_by('resolution').desc()

        if len(available_streams) > 0:
            print("Доступные варианты качества видео:")
            for i, stream in enumerate(available_streams):
                print(f"{i+1}. {stream.resolution}")

            print("0. Скачать видео в формате MP3")

            choice = input("Выберите номер варианта качества или введите '0' для скачивания в формате MP3: ")

            if choice == "0":
                filename = input("Введите имя файла для сохранения аудио (без расширения): ")
                full_filename = f"{filename}.mp3"

                print("Конвертация видео в аудио...")
                video = YouTube(url).streams.get_highest_resolution().download(filename="temp")
                video_clip = VideoFileClip(video)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(full_filename)
                audio_clip.close()
                video_clip.close()
                os.remove(video)
                print("Аудио успешно скачано в формате MP3.")
            else:
                index = int(choice) - 1

                if 0 <= index < len(available_streams):
                    selected_stream = available_streams[index]
                    print(f"Выбрано качество {selected_stream.resolution}.")

                    filename = input("Введите имя файла для сохранения (без расширения): ")
                    file_extension = selected_stream.mime_type.split("/")[-1]
                    full_filename = f"{filename}.{file_extension}"

                    print("Скачивание видео...")
                    selected_stream.download(filename=full_filename)
                    print("Видео успешно скачано.")
                else:
                    print("Неверный номер варианта качества.")
        else:
            print("Не удалось найти доступные варианты качества видео.")
    except Exception as e:
        print("Произошла ошибка при скачивании видео:", str(e))

download_youtube_video()
