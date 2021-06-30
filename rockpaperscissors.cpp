#include <iostream>
using namespace std;

void you_win()
{
    cout << "You win!" << endl;
}


void you_lose()
{
    cout << "You Lose :(" << endl;
}

void you_tie()
{
    cout << "That's a tie!!" << endl;
}

int main()
{
    cout << "1. Paper" << endl;
    cout << "2. Rock" << endl;
    cout << "3. Scissors" << endl;
    cout << "What is your choice: ";
    int player_choice;
    cin >> player_choice;
    cout<< endl;

    srand(time(NULL));
    int comp_choice = rand() % 3 + 1;

    if (player_choice == 1)
    {
        cout << "Your choice is: Paper" << endl;
        cout << "Computer choice is: ";
        if (comp_choice == 1)
        {
            cout << "Paper" << endl;
            you_tie();
        }
        else if (comp_choice == 2)
        {
            cout << "Rock" << endl;
            you_win();
        }
        else
        {
            cout << "Scissors" << endl;
            you_lose();
        }
    }

    if (player_choice == 2)
    {
        cout << "Your choice is: Rock" << endl;
        cout << "Computer choice is: ";
        if (comp_choice == 1)
        {
            cout << "Paper" << endl;
            you_lose();
        }
        else if (comp_choice == 2)
        {
            cout << "Rock" << endl;
            you_tie();
        }
        else
        {
            cout << "Scissors" << endl;
            you_win();
        }
    }


    if (player_choice == 3)
    {
        cout << "Your choice is: Scissors" << endl;
        cout << "Computer choice is: ";
        if (comp_choice == 1)
        {
            cout << "Paper" << endl;
            you_win();
        }
        else if (comp_choice == 2)
        {
            cout << "Rock" << endl;
            you_lose();
        }
        else
        {
            cout << "Scissors" << endl;
            you_tie();
        }
    }

}
