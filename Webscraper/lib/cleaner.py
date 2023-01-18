import os

class cleaner:
    path = "Webscraper/results/"
    max_Files = 50

    def __init__(self) -> None:
        pass

    def sorted_ls(path):
        mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
        return list(sorted(os.listdir(path), key=mtime))

    def run(self):
        del_list = self.sorted_ls(self.path)[0:(len(self.sorted_ls(self.path)) - self.max_Files)]

        for dfile in del_list:
            os.remove(self.path + dfile)