from pullDailyInput import GetDailyData
import sys
import importlib.util

def run_script(script_path, input_text):
    spec = importlib.util.spec_from_file_location("my_script", script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["my_script"] = module
    spec.loader.exec_module(module)
    module.main(input_text)


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("input a day")
        exit(-1)

    day = sys.argv[1]
    GetDailyData(day)
    script_path = f'days/{day}.py'

    with open(f'./inputData/inputDay{day}.txt') as file:
        inputText = file.readlines()

    # Sanitize
    for x in range(len(inputText)):
        inputText[x] = inputText[x].replace('\n','')
        
    run_script(script_path, inputText)
