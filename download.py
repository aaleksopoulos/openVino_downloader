import os, platform, argparse

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Python script to help download free OpenVINO models")

    # -- Create the descriptions for the commands
    i_desc = "The location of the install directory, skip it if installed in default"
    o_desc = "The path to the output file, skip if you want to download in the downloader folder"
    p_desc = "The precision of the model, skip if you want to download all precisions"
    n_desc = "The name of the model, skip if you want to download all avaiable free models"

    # -- Add required and optional groups
    parser._action_groups.pop()
    #required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    # -- Create the arguments
    optional.add_argument("-i", help=i_desc, default=None)
    optional.add_argument("-o", help=o_desc, default=None)
    optional.add_argument("-p", help=p_desc, default=None)
    optional.add_argument("-n", help=n_desc, default=None)
    args = parser.parse_args()

    return args

def main():
    #get the arguments
    args = get_args()

    if args.i is None:
        #check which os we are using
        if (platform.system()) == "Windows":
            inst_dir = "C:/Program Files (x86)/IntelSWTools/openvino/"
        else:
            inst_dir = "/opt/intel/openvino/"
    else:
        inst_dir = args.i

    #path to where the downloader.py is
    downloader_path = "deployment_tools/open_model_zoo/tools/downloader"
    down_folder = os.path.join(inst_dir, downloader_path) #complete the path to the downloader.py
    print(down_folder)

    if os.path.isdir(down_folder):
        print("folder containing dowloader.py  found, proceeding to download")
    else:
        print("folder containing dowloader.py not found, exiting")
        exit(1)

    #placeholder for the parameter list
    par = []
    #let's contstruct the command
    #get the name of the model
    if args.n is None:
        s1 = "--all"
    else:
        s1 = "--name " + args.n
        print(s1)
    par.append(s1)
    
    #get the precision
    if args.p is not None:
        s2 = "--precisions " + args.p
        par.append(s2)
    
    #get the output folder
    if args.o is not None:
        s3 = "-o " + args.o
        par.append(s3)

    #convert the paramateres to str
    pars = " ".join(par)

    down_cmd = "python downloader.py " + pars
    #print(down_cmd)
    
    #change folder to run the downloader
    os.chdir(down_folder)
    os.system(down_cmd)


if __name__ == "__main__":
    main()