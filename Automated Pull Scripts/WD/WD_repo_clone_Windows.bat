@echo off
REM Cloning the repository with sparse checkout
git clone --filter=blob:none --sparse https://github.com/HyperionDevBootcamps/Lecture-Backpack-1.git

REM Changing directory to the cloned repository
cd Lecture-Backpack-1

REM Adding the specific folders to sparse checkout
git sparse-checkout add "Full Stack Web Development (WD)"
git sparse-checkout add "StarterPack"

@echo on
