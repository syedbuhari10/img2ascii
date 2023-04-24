import os
import glob
import shutil
import sys
import ffmpeg
from pdb import set_trace

def run_vid_to_frames(video, fps):
    path = os.getcwd()
    frames_path = os.path.join(path, "frames")
    is_frames_exists = os.path.exists(frames_path)
    # set_trace()

    if not is_frames_exists:
        os.makedirs(frames_path)

    is_frames_empty = False
    if len(os.listdir(frames_path)) == 0:
        is_frames_empty = True
        print(os.listdir(frames_path))

    if not is_frames_empty:
        for file in glob.glob(os.path.join(frames_path, "*")):
            os.remove(file)
        print("frames emptied")

    try:
        (ffmpeg.input(os.path.join(path, "lagtrain.mp4"))
            .filter('fps', fps=fps)
            .output(os.path.join(frames_path, "%d.jpg"),
                    video_bitrate="5000k",
                    s='64x64',
                    sws_flags="bilinear",
                    start_number=0)
            .run(capture_stdout=True, capture_stderr=True))
        print("Video_to_frames ran successfully!!")
    except ffmpeg.Error as e:
        print('stdout:', e.stdout.decode('utf8'))
        print('stderr:', e.stderr.decode('utf8'))

# run_vid_to_frames("lagtrain.mp4")