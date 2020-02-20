# Welcome to the OGHPC Devito-GPU hackathon


That's enough of the pleasantries. Let us get started.

## Step 1: Get account and GPU enabled VM for development
You need to click on this link:
https://labs.azure.com/register/jltt9mv2

You will be redirected to your Azure Labs VM.
There you can set your password for logging in to your VM.
You have to wait for a minute or so.
When your password is updated, click on the screen emoji at your VM and select
`Connect via SSH`. Copy the ssh command to your terminal
and start hacking!

## Step 2: Enroll in the hackathon
Click on this link to enroll
https://classroom.github.com/a/LYAlBqE_
This is going to give you a unique github repo which you should clone on the VM created above.

## Step 3:
In the repository that you have just cloned, you will find two Python files.
One of these is `run-preset.py`, which allows you to execute a set of Devito
benchmarks that we have pre-selected for this hackathon. Aspects like
discretization and duration of the benchmark are fixed, so you won't care about
them. The only argument that `run-preset.py` accepts is the name of the
benchmark -- there are four alternatives, listed below by increasing order of
generated-code complexity:

* `python run-preset.py acoustic`: to generate and run an isotropic acoustic
  forward propagator.
* `python run-preset.py tti`: to generate and run an anisotropic (TTI) acoustic
  forward propagator.
* `python run-preset.py tti-agg`: like above, but Devito will now optimize the
  generated code to perform fewer FLOPs, in exchange for a larger working set.
* `python run-preset.py viscoelastic`: to generate and run a visco-elastic
  forward propagator.

The first time you run the command, the code gets generated. Instructions will
be provided on screen explaining how to hack the generated code. Then, to test
your hacking, just re-run the same command. Performance metrics (e.g.,
completion time, GFlops/s performance) will be displayed by Devito on screen at
the end of each run.

## Step 4:
To submit your work at the end of the hackathon, just run `python
push-files.py`.  And that's it!

## Step 5:
TODO @navjot - look at league table. @navjot to write benchmarking script.
