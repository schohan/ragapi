import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileProcessor(FileSystemEventHandler):
    def __init__(self, watch_dir):
        self.watch_dir = watch_dir

    def on_created(self, event):
        """
        Called when a new file is detected in the watch directory.
        """
        if not event.is_directory:
            file_path = event.src_path
            print(f"File detected: {file_path}")
            self.process_file(file_path)

    def process_file(self, file_path):
        """
        Placeholder for processing a file. After processing, the file is deleted.
        """
        try:
            print(f"Processing file: {file_path}")
            # Simulate file processing (replace with actual processing code)
            time.sleep(2)
            print(f"Finished processing: {file_path}")

            # Delete the file after processing
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except Exception as e:
            print(f"Failed to process {file_path}: {e}")

    def start_watching(self):
        """
        Start the observer to watch the directory for new files.
        """
        observer = Observer()
        observer.schedule(self, self.watch_dir, recursive=False)
        observer.start()
        print(f"Started watching folder: {self.watch_dir}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()


# write a main method
if __name__ == "__main__":
    watch_dir = "watch_dir"
    file_processor = FileProcessor(watch_dir)
    file_processor.start_watching()