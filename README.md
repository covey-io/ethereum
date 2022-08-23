
# Getting Started
***
1. C++ Build Tools (in case not already on your machine - frequently seen with Windows Users)
[download here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

2. Create a project folder in your file system **folder_name**

3. Using the terminal of your choice, create a virtual python environment within **folder_name**.

    `python3 -m venv env` [^1]
    
4. Activate the virtual environment.

    windows `source env/Scripts/Activate` [^2]

    mac `source env/bin/activate` [^2]
 

5. Once the environment is activated (the terminal should have the environment name pop up in front of the user name as **(env)**), proceed to install the covey-sdk.
    `pip install covey-sdk`

6. If there are no errors, you are ready to open the project in Visual Studio Code.
- Open VS Code and go to **File > Open Folder** *(choose the project)*.
- Make sure the **env/** folder is visible in the project structure.

7.  Although it should be a default, make sure the proper interpreter is selected from the **env/** folder
- Click `Ctrl + Shift + P` and type in **Python : Select Interpreter** in the drop down.
- The proper interpreter will be in the **env/scripts** folder and will have a star next to it.

8. Create a new file called test.py or whichever name you would prefer and run the following code

    `import covey.covey_trade as ct`

    `t = ct.Trade(address = <public wallet key>, address_private = <private_wallet_key>, posting_only = True)`
    
    `t.post_trades_polygon('FB:0.25')`

[^1]: note you can call it env or venv just something conventional to remember, also important to use the command **python3** to make sure the proper version is installed in the virtual environment.

[^2]: again note that 'env' is just a name we used to name our virtual environment. You can call it covey_env or something custom if you wish.


9. Note the post trades string needs to be one string with the format '<ticker>:<allocation>,<ticker>:<allocation>,...'

If successful, the terminal should write back that your trades have been posted.

Please let us know if you have any questions or run into issues, happy coding!