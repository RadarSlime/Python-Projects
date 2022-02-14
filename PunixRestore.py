from sys import stdout, argv
import os
from shutil import rmtree

help_data = 'add [varname] [varvalue]\nHow to use add:\n    add will create a system variable called [varname]. If you type %[varname] it will replace %[varname] with [varvalue]%%%%%%List of commands:\n    help   - displays infomation of a command\n    echo   - repeats and input\n    dump   - displays a file\n    edit   - primitive file editing\n    cls    - clears the screen\n    cd     - Enter working directory\n    ld     - Leave directory\n    mkdir  - makes a directory\n    mkfile - makes a file\n    rmv    - removes a file or folder\n    move   - moves a file\n    rename - renames a file\n    add    - adds a variable (Refer to them using %[variabke name])\n    set    - sets the value of a variable (do not use %)\n    del    - rmeoves a variable (do not use %)\n    if     - conditionals\n    write  - writes to a file\n    clear  - clears a file\n    rep    - repeats an action\n    for    - repeats an action and sets %a to a filename (view the help page)\n    btp    - convets a txt file into a pnx file (ONLY FOR ADVANCED USERS)\n\nFor further infomation type help [commandname] (e.g. "help echo")%%%%%%btp [file]\nHow to use btp:\n    btp will convert a .txt file into a .pnx file\n    you can run .pnx files from the command line as if they were a built in command\n\n    [ONLY FOR ADVANCED USERS]%%%%%%cd [path]\nChanges the working directory to path\n   cd downloads means all operations will be done inside of downloads%%%%%%clear [file]\nhow to use clear:\n    clear will clear [file]\n    No data will be left\n    \n    [ONLY FOR ADVANCED USERS]%%%%%%cls\n   Will clear the screen%%%%%%del [varname]\nHow to use del\n    del will delete a variable\n    >add egg 10\n    >echo %egg\n    10\n    >del egg\n    >echo %egg\n    %egg             : egg variable gone%%%%%%dump [path] *[format]\nHow to use dump:\n    the file name after dump will have all its contents displayed to the console.\n    format is usually retrieved automatically but you can override it using:\n        --raw   | -r : displays all the text\n        --basic | -b : formats the text to display properly with Punix text editor%%%%%%echo [words...\nHow to use echo?\n    Simply type something after echo and it will say it\n%%%%%%edit [path]\nHow to use the Punix text editor:\n    To add a line simply type said line.\n    You can set a line number by prefixing the line with a number.\n    Save by typing @w.\n    To leave the editor without saving, type @q. To leave and save, type @wq.\n\nEXAMPLES:\n    10 Hello world    - Would right Hello world at line ten (blank lines are ignored)\n    5 Sup peeps       - Would put Sup peeps at line 5 which is before ten, meaning it would show before hello world.\n    5 Formal          - Would overwrite Sup peeps with Formal\n    @wq               - Would save the file and quite the program.%%%%%%for [path (can be blank)] do [code]\nhow to use for\n    for will act just like rep but will instead loop of every item in [path]\n    %a will equal the current file the code is on and %i will equal the iteration\n    "for temp do rmv %a" would delete everything inside temp%%%%%%Bruh why, like what did you think this would do?%%%%%%if [condition] [code]\nHow to use if:\n    if will only run [code] if [condition] is true\n    condition can not have any spacebars\n    Valid: 1==1\n    Invalid : 1 == 1\n    Possible operators are:\n        ==   equal\n        <    less\n        >    greater\n        <-   inside\n        <!   not inside\n    for example:\n    >if data<-dat echo data contains dat\n    data contains data\n\n    >if data==data echo data\n    data\n\n    >if 4<5 echo 4<5\n    4<5%%%%%%ld\nReturns to the previous directory\n   C:/downloads/ -> ld -> C:/\n%%%%%%mkdir [path+name]\n    will create a directory%%%%%%mkfile [path+name]\n    will create a file at path with the name [name]\n    to edit these files use the punix editor%%%%%%move [file] [directory]\nHow does Move work:\n    move moves [file] into [directory] easy file moving B)%%%%%%rename [file] [new_name]\nHow does rename work:\n    rename will change the name of [file] to [new_name]\n    it is reccomend to NOT use rename from outside the directory containing [file] unless you understand the code behind punix%%%%%%rep [iterations] [code]\nHow to use rep:\n    rep will reapeat [code] [iterations] times. %i will equal the iteration the code is currently on.\n    code could be anything (it is recommended to not use for or rep inside)\n    >rep 10 echo %i\n    1\n    2\n    3\n    4\n    5\n    6\n    7\n    8\n    9\n    10%%%%%%rmv [path]\n    will delete a file or folder off of punix%%%%%%set [varname] [varvalue]\nHow to use set:\n    set will change the value of a pre existing variable\n    add egg 10    : %egg = 10\n    set egg 12    : %egg = 12%%%%%%write [file] [text]\nHow to use write:\n    write will write [text] to [file]'.split("%%%%%%")
help_names = ["add", "all", "btp", "cd", "clear", "cls", "del", "dump", "echo", "edit", "for", "help", "if", "ld", "mkdir", "mkfile", "move", "rename", "rep", "rmv", "set", "write"]

def out(word, end="\n"):
    stdout.write(word + end)
    stdout.flush()

def del_o(path):
    if os.isdir(path):
        rmtree(path)
    else:
        os.remove(path)

ok = "FINE"
mc = "MEMORY CORRUPTION"
fo = "FOREIGN OBJECT"
def check_disk(path):
    Checks = ok
    while 1==1:
        if not os.path.exists(path):
            Checks = mc
            break
        if not os.path.exists(path + "/Users"):
            Checks = mc
            break
        if not os.path.exists(path+"/Help"):
            Checks = mc
            break
        if not os.path.exists(path+"/ExtraCommands"):
            Checks = mc
            break
        if not os.listdir(path+"/Help") == ['add.txt', 'all.txt', 'btp.txt', 'cd.txt', 'clear.txt', 'cls.txt', 'del.txt', 'dump.txt', 'echo.txt', 'edit.txt', 'for.txt', 'help.txt', 'if.txt', 'ld.txt', 'mkdir.txt', 'mkfile.txt', 'move.txt', 'rename.txt', 'rep.txt', 'rmv.txt', 'set.txt', 'write.txt']:
            Checks = mc
            break
        if not len(os.listdir(path)) == 3:
            Checks = fo
        break
    return Checks

out("=" * 30)
out("WELCOME TO PUNIX RESTORE!")
out("=" * 30)
out("Running internal checks...")

path = "C:/punix/PunixData/"
checks = ["ExtraCommands","Help","Users"]

if len(argv) == 2:
    path = argv[1]

EC_status = False
H_status = False
U_status = False

items_removed = 0

for i in os.listdir(path):
    if i == checks[0]:
        out("found: ExtraCommands")
        EC_status = True
    elif i == checks[1]:
        out("found: Help\nChecking status of Help...", "")
        if len(os.listdir(path + "/" + checks[1])) != len(help_names):
            out("=corrupted")
            for helpfile in os.listdir(checks[1]):
                del_o(path + helpfile)
        else:
            out("good")
            H_status = True
    elif i == checks[2]:
        out("found: Users")
        U_status = True
    else:
        items_removed += 1
        out("removing foreign item: " + i + "...", "")
        del_o(path + i)
        out("Done")

out(str(items_removed) + " items removed")
out("=" * 30)
if not EC_status:
    out("Restoring: ExtraCommands...", "")
    os.mkdir(path + checks[0])
    out("Done")
if not H_status:
    out("Restoring: Help...", "")
    hpath = path + checks[1]
    os.mkdir(hpath)
    i = 0
    while i < len(help_names):
        open(hpath + "/" + help_names[i] + ".txt", "w").write(help_data[i])
        i += 1
    out("Done")
if not U_status:
    out("Restoring: Users...", "")
    os.mkdir(path + checks[2])
    out("Done")

if EC_status and H_status and U_status:
    out("No Errors Found")

out("=" * 30)
result = check_disk(path)
if result == ok:
    out("Restoration Complete")
else:
    out("Restoration failed, error = " + result)
out("=" * 30)

