import passwordGenerator as pwg
import tkinter as tk


def main():
    root = tk.Tk()
    root.title = "Password generator"

    root.minsize(200, 200)
    root.maxsize(500, 300)
    root.geometry("300x300+50+50")

    entry = tk.Entry(root)
    entry.insert(0, "")
    #entry.bind("<Return>", return_pressed)
    entry.pack(padx=10, pady=10, fill="x")
    def on_click():
        entry.delete(0, 'end')
        password = pwg.generatePassword(3,12)
        entry.insert(0, password)

    generatePassphrase = tk.BooleanVar()
    passphrase = tk.Checkbutton(root, text="Generate passphrase", var=generatePassphrase)
    passphrase.pack(padx=20,pady=20)
    button = tk.Button(
        root,
        text="Generate",
        command=on_click,
    )
    button.pack(padx=15,pady=10)


    # A helper label to show the selected value
    label = tk.Label(root, text="Entry demo!")
    label.pack(padx=5, pady=5, fill="x")
    root.mainloop()

if __name__== "__main__":
    main()