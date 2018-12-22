from app.controller.programInit import *

def main():
    program = AppController()
    program.iconify()
    program.update()
    program.deiconify()
    program.mainloop()
    program.destroyer()
    program.destroy()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())