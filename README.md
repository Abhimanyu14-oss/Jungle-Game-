# **Jungle Game**

Welcome to **Jungle Game**! 🐾 Embark on a thrilling journey filled with unexpected twists and challenges. Will you survive the jungle and emerge victorious? Let's find out!

---

## 🎮 How to Play

1. Run the program.
2. Follow the on-screen instructions to make your choices:
   - Press **1** or **2** to make decisions.
   - Navigate the jungle carefully to avoid deadly traps!
3. Survive and reach the final victory, or face the dangers of the wild.

---

## 🧩 Game Flow

- Choose your path: Left or Right.
- Encounter soldiers, animals, and strangers.
- Every decision has consequences—choose wisely.
- Win by trusting the right stranger or face the dangers of the jungle.

---

## 🔧 Code Walkthrough

```python
print("Jungle Game")

def final_call():
    x = int(input('''Do you want to play again \n Yes-1 No-2\n 1::'''))
    if x == 2:
        print("Thanks for playing")
    else:
        options()

def options():
    a = int(input("Press 1====>Left \n Press 2====>Right \n"))
    if a == 2:
        print("Again two options")
        y = int(input("Press 1====>Left \n Press 2====>Right \n"))
        if y == 2:
            print("Killed by soldier====>Game over")
            final_call()
        elif y == 1:
            print("Want to take stranger's help???")
            z = int(input("Press 1====>Yes \n Press 2====>No \n"))
            if z == 1:
                print("Stranger saves you=====>Congratulations! You won")
                final_call()
            else:
                print("You trapped ====>Game over")
                final_call()
    elif a == 1:
        b = int(input("Press 1====>Turn Left \n Press 2====>Turn Right \n"))
        if b == 1:
            print("You have fallen in a pit=====>Game over")
            final_call()
        else:
            print("You have been killed by an animal====>Game over")
            final_call()

options()


🚀 Features

Interactive gameplay.

Decision-based outcomes.

Simple text-based interface.

🐍 Requirements
Python 3.x

📜 License
This project is open-source and available under the MIT License.
