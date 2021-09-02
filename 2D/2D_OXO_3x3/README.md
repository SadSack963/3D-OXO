# Noughts and Crosses (Tic-Tac-Toe)

<img src="./images/tic-tac-toe.png">

<h2>The classic game of Tic-Tac-Toe.</h2>
<p>
    An executable file created by     
    <a href="https://pypi.org/project/auto-py-to-exe/">
        auto-py-to-exe
    </a> 
    can be downloaded from 
    <a href="./executable/oxo_2d.exe">
        oxo_2d.exe
    </a>
</p>
<p>
    The initial screen allows you to choose the players. 
    This is a Tkinter window. 
    When closed it passes the player dictionary back to the main code.
</p>
<p>
    A Turtle Graphics window then opens, and you can play the game.
    <i>Good luck beating the computer!</i> 😎
</p>
<p>
    This is my first working implementation of the game coded from scratch after learning Python at the excellent Udemy course: 
    <center>  
        <h2>
            <a href="https://www.udemy.com/course/100-days-of-code/">
                    100 Days of Code - The Complete Python Pro Bootcamp for 2021
            </a>
        </h2>
        by Angela Yu.
    </center>  
</p>
<h2>
    The development process
</h2>
<p>
    I first got the main concept code working using a numpy array to store the game state.
    I used a simple text interface in the console, so that I could type in an array location and then print out the array so that I could see the move. 
    I tested several scenarios using the built in unittest module to make sure my game state evaluation was correct.
</p>
<p>
    Then I needed to get the computer working as an opponent. 
    This led me to research the Minimax Algorithm. 
    I actually got that working quite quickly, but a stupid bug where the computer sometimes chose the wrong move held me up for a couple of days, while I tried to track down what was going on. 
</p>
<p>
    <b>
        <i>Believe me, manually tracking and debugging the minimax tree is a real PITA!</i>
    </b>
    Again the unittest module helped a lot with various scenarios, making sure the AI chose the correct move for a given starting position.
</p>
<p>
    Next came the task of creating the GUI. 
    I wanted to start with stuff we had already learned on the course, so I went with Turtle Graphics.
    The implementation was pretty straightforward. 
    The hardest part was figuring out how to detect which section of the grid the mouse was clicked in, 
    and getting the correct coordinates for drawing the X's and O's.
    I was right chuffed when it all came together, and I could click on the screen to make a move... and the AI made a move in reply! :)
</p>
<p>
    Now, I needed a way for the user to choose players. 
    For this I decided to use a standard Tkinter window.
    That was easy, and it tested just fine in isolation.
</p>
<p>
    However, when I integrated it into my project, there was a problem. 
    I found that although the widgets appeared to work, the player dictionary wasn't being altered from the default values.
    I noticed that a blank Turtle window was opening just before the Tkinter window. 
    This was obviously interfering with the Tkinter code.
    It took me a while to refactor my code such that the Tkinter window appeared first, without the Turtle Graphics window opening.
</p>
<p>
    The final step was to get some messages appearing on the Turtle window. 
    For this, I created a Messenger class, which worked fine in isolation.
    However, the same problem occurred again when I integrated it into the project. 
</p>
<p>
    This time, it was caused by the inheritance of the Turtle class. 
    I finally realised that simply initialising the super().__init__() method was creating a turtle, and in the process was creating a new Turtle Graphics window!
    So I had to delay that initialisation until after the Tkinter window had closed.
</p>
<h2>
    Future development
</h2>
<p>
    So, that's where I'm up to at the moment. 
    I have also discovered a method which I could use to integrate Tkinter widgets into a Turtle Graphics screen, so that will be my next small step.
</p>
<p>
    Following that, I want to get the graphics working in PyGame or Kivy. 
    That could be a useful learning exercise for the future.
</p>
<p>
    My ultimate aim is to create a 3D version, using a 4x4x4 array (or more). 
    The first step on this path will be to extend this version to a 4x4 grid.
    Then use 4 separate grids, still displayed in 2D, to get a working game.
</p>
<p>
    The final step, and I predict the most difficult, will be to create a rotatable cube in 3D space. 
    There are a few 3D engines for Python, but I haven't done any real investigation yet. 
    Hopefully, I won't need to brush up my matrix manipulation too much!
</p>
<p>
    Time will tell how far I get along this road, but I am looking forward to the journey. 😀
</p>
