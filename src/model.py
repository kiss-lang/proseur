from faster_whisper import WhisperModel
from sys import argv

model_size = argv[1]
device = argv[2]
compute_type = argv[3]
language = argv[4]

if __name__ == "__main__":
	model = WhisperModel(model_size, device=device, compute_type=compute_type)

	while True:
		next_file = input()
		segments, info = model.transcribe(next_file, language=language)

		for segment in segments:
			print(segment.text)