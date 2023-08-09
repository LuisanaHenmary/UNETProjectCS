from components.root_window import RootWindow
from views.app import App

if __name__=="__main__":
    root = RootWindow()
    notebook_pag = App(root)
    root.mainloop()
