First of all, you need to configure your computer to init with the rtc;
After that, use the windows schedule to set a activity to every day at the time
what you want to shutdown the computer;
in the activity mark the option:
"Execute with user connected or not"
If not possible, make sure thats is active in the gpedit.msc
Windows config > local Polity > user Rights Assigment > Log on as batch job > include the user 