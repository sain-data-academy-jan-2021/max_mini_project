#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def rate_sys(connection):
    rate = input(
        "Thankyou for your order. Would you mind leaving a review for us today? "
    )

    rate_y = ["Yes", "yes", "y", "Y"]
    rate_n = ["No", "no", "n", "N"]
    rate_stars = [1, 2, 3, 4, 5]

    if rate in rate_y:
        cursor = connection.cursor()
        rate_name = input("Thankyou! What is your username?: ")
        rate = int(input("And how many stars out of 5 would you give our service? "))
        cursor.execute(
            f'INSERT INTO ratings (username, rating) VALUES ("{rate_name}", {rate})'
        )
        connection.commit()
        print("Thanks, we'll take that onboard. Until next time!")
        cursor.execute("select * from ratings")
        ratingtable = cursor.fetchall()
        username = []
        rating = []
        color_list = []
        sum = 0
        for row in ratingtable:
            username.append(row[1])
            rating.append(row[2])
            color_list.append("b")
            sum += row[2]
        username.append("AVERAGE")
        rating.append(float(sum / len(ratingtable)))
        color_list.append("r")

        x_pos = np.arange(len(username))
        plt.bar(x_pos, rating, color=color_list)
        plt.xticks(x_pos, username)
        plt.ylabel("Rating")
        plt.xlabel("Usernames")
        plt.title("User Ratings")
        plt.show()
    elif rate in rate_n:
        print("Ok no problem. Until next time!")
    else:
        print("Sorry, invalid selection. Please try again.")
    return rate


# %%
