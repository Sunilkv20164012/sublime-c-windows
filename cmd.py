import os, sublime_plugin
class CmdCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        path=file_name.split("\\")
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        compiling =  "echo \"compiling....        \" "
        running   =  "echo \"running......        \" "
        finished =   "echo ___________________________________________________________________________________________________"
        command= "cd "+current_directory+" & "+current_driver+" & " + compiling + " & C:/MinGW/bin/g++ basic.cpp & " + running + " & a.exe & " + finished + " & pause " 
        os.system(command)
        
