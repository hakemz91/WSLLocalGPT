import os

# Path to the bashrc file
bashrc_path = os.path.expanduser("~/.bashrc")

# Code to be added to bashrc
bashrc_code = """
# Activate Conda environment
conda activate WSLLocalGPT

# Function to run commands
function run_commands() {

echo -e "\e[38;5;214m1. Chat(No History = No Memory)\e[0m"  
echo -e "\e[38;5;117m2. Chat(With History = Memory -> But beware of limited context windows)\e[0m"
echo -e "\e[38;5;118m3. Ingestion\e[0m"
echo -e "\e[38;5;227m4. Ingestion(auto shutdown PC after finish)\e[0m"

read -p "Enter the number of the command: " choice

case $choice in

1)
echo -e "\e[38;5;214mRunning Option 1: Chat(No History = No Memory)\e[0m"
python run_localGPT.py --model_type mistral
;;

2) 
echo -e "\e[38;5;117mRunning Option 2: Chat(With History = Memory -> But beware of limited context windows)\e[0m"
python run_localGPT.py --model_type mistral --use_history
;;

3)
echo -e "\e[38;5;118mRunning Option 3: Ingestion\e[0m"  
python ingest.py
;;

4)
echo -e "\e[38;5;227mRunning Option 4: Ingestion(auto shutdown PC after finish)\e[0m"
python start_date.py && python ingest_AS.py && python finish_date.py && python autoshut.py  
;;

*)
echo "Invalid choice. No command will be executed."
;;

esac

read -p "Do you want to run another command? (y/n): " confirm 

if [ "$confirm" == "y" ]; then
run_commands  
else
echo "Exiting..."
fi

}

# Run the commands function
run_commands
"""

# Append code to bashrc
with open(bashrc_path, "a") as bashrc_file:
    bashrc_file.write(bashrc_code)

print("Code added to ~/.bashrc file.")
