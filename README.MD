# Automatic Streaming Highlights

In a nutshell: Have you ever wanted to magically create a short video including all the highlights of your 7-hour Twitch video? Well, you have come to the right place. 

(Most of the information put here comes from my comments from the Jupyter Notebook)

This short repository (in development) contains a new feature for my **Automatic Gaming Sharing Tools** project (name can change during development). 

## FAQ

1. How does the algorithm work?

    The algorithm takes as input the whole video and it returns a short video that is basically each highlight found by the algorithm concatenated next to each other.

2. What does "highlight" means in this context?
    
    Similar to Zulko's implementation, a highlight for me in this case means **a very loud/noisy moment** during gameplay. As a brief example, usually when I play with my friends Halo Infinite, we tend to get very loud during certain matches or when we perform some objectives in the game. Another example would be a commented fighters videogame tournament where both commenters and players get very loud when a certain fantastic, wild moment occurs.

3. How many "highlights" or "loud moments" are taken into account? 

    This is an example from a graph created in a certain step by the algorithm using a 40min Fall Guys video:
    ![Fall Guys Average Volumes](img/volumesPlot.png)
    
    As we can see, there are some higher peaks through the whole video, by default, the algorithm takes into account the top 10% of the peaks and puts them in the highlights video. The selection of the peaks can be changed via the **peaks_times** variable found in the Jupyter Notebook.

4. Can I also automatically share this automatically created video? 

    This is currently a feature I'm working on. I plan to make possible the automatic upload to Youtube, Twitter and Instagram.

5. Can I only run this algorithm via Jupyter Notebook?

    You can run this algorithm also via command line python scripting. I'm also working on a simple desktop app to perform the automatic streaming highlights without going into the code. 

# Jupyter Notebook and Overview

The Notebook contains my experiments and my custom implementation using the code from Zulko's Automatic Soccer Highlights [1] in order to use it for my gaming streamings and my new project **Automatic Gaming Sharing Tools** which is a subtask of the **Automatic Video Uploader** project.

Similar to Zulko's implementation, I would like to make a video summary of a previously saved streaming video game, using the fact that myself and my friends (in the video that we recorded) usually scream, tend to be louder when something interesting happens. By this explained fact, in this project I select as a metric for my gaming highlights the **noisiness** of my clips in order for them to be put in the video. In other words, the loudest moments of the streaming will be the most considered to be put in the video summary, which is also the same metric that is used in the Zulko's algorithm.

At the moment, I'm also working on another metrics for **Automatic Gaming/Streaming Highlights** based on specific in-game sounds that specify a possible highlight as a multikill, objective complete in Halo Infinite using **speech recognition** and the text recognition of the same events such as reading **DOUBLE KILL, OBJECTIVE COMPLETE** directly from the video input using **text recognition**. The repo for that project can be found [here](https://github.com/spolo96/gaming-text-speech-recognition).

# Usage

At the moment, the algorithm can only be run via Jupyter Notebooks (or via script if you want). As said in the answer for the question 5 in **FAQ**, a solution to use the algorithm as a desktop app is in development. 

## Dependencies 

The following libraries/modules are required for the project:

- Jupyter Notebook (heavily recommended to see the code and visualize the volumes)
- Matplotlib
- Numpy 
- MoviePy

There are several ways to install Jupyter Notebook, they are found [here](https://jupyter.org/install)

You can install them via pip:
```
  pip install notebook
```
```
  pip install matplotlib
```
```
  pip install numpy
```
```
  pip install moviepy
```

After everything is installed, we can just open the **Automatic Streaming Highlights** Notebook and run every cell, changing some lines to include directory/paths to your need (these suggestions are also in the Notebook):

- ```os.chdir([PATH_OF_YOUR_VIDEO]) # Path of video directory, e.g: "/c/Users/User/Videos/VODs/Fall_Guys"```
- ```videoFileName = "streaming2p3.mp4" # Video Name Example ```
- ```peaks_times = peaks_times[peaks_vols>np.percentile(peaks_vols,90)] # You can change the 90 with 80, 70, ... in order to include more highlights or not.``` 

# Conclusions

This simple method works very well spotting gaming highlights using the **noisiness** metric in the volume of the video. A simple highlight video example that I created using this algorithm can be found here: [Dragon Ball FighterZ example](https://www.youtube.com/watch?v=iJ1P0avtbDs&list=PLwAjkPGn41YWQlKNZ8maq5G9H5dCjKuPx) (The original video was 3 hours of content and the algorithm gave us a 10 minute video with all the highlights, saving us a lot of time checking the video again, finding all the possible highlight moments and putting them in a single video.)

As Zulko said in [1], (talking about the original video which was a soccer game): "The algorithm can be confused by broadcasters which make lots of replays or lower the sound of the crowd after goals, and it may miscut some goals on penalties, because the crowd starts whistling long before the shoot. So large-scale applications would require a less naive model."

The algorithm can be confused in these situations, but the solution itself already saves us an intense amount of time finding the possible highlights of the game/video of interest. Since the loudest times can be selected in the **peaks_times** variable and the **final_times** variable contains the times (in seconds) of these events, we can manually check around the times in the array of **final_times** to find other possible highlights that the model couldn't find saving us a lot of time since we already know where to look at, instead of watching the whole video from start which could be very troublesome for very long videos as we can normally find in Twitch. 

# References 

I infinitely would like to thank [Zulko](https://github.com/Zulko) for the **moviepy library** and this [1] specific algorithm to perform the automatic streaming highlight. This library is what made possible my ideas and projects for **Automatic Video Uploader** and **Automatic Gaming Sharing Tools**. I have learned a lot working on these projects especially **code automation** which is one of my favorite topics to make our life easier and it has been quite an adventure thanks to you.

[[1] Automatic Soccer Highlights Compilations With Python](http://zulko.github.io/blog/2014/07/04/automatic-soccer-highlights-compilations-with-python/)

[[2] MoviePy](https://zulko.github.io/moviepy/)