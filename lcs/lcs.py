import sys
import os

def build_lcs_matrix(str1, str2):
    m = len(str1)
    n = len(str2)
  
    #initialize the lcs_matrix
    lcs_matrix = [[0] * (n+1) for i in range(m+1)]
  
    #fill in the matrix
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs_matrix[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])
    

    return [lcs_matrix,m,n]
  
#get the longest subsequence
def build_lcs(lcs_matrix,m,n):
    index = lcs_matrix[m][n]
    
    lcs_sequence = [""] * (index)

    i = m
    j = n
    while i > 0 and j > 0:
  
    #if current character in str1[] and str2[] are the same, then it is part of lcs
        if str1[i-1] == str2[j-1]:
            lcs_sequence[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
  
    #if not same, then find the larger of two and go in the direction of larger value
        elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
  
    return "".join(lcs_sequence)
  
#test the algorithm with example input

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().lower()
        return content

# Get the directory path of this Python file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create the file paths using the directory path
str1 = read_file(os.path.join(dir_path, "test1.txt"))
str2 = read_file(os.path.join(dir_path, "test2.txt"))

output_file = os.path.join(dir_path, "result.txt")

# Redirect the standard output to the output file
with open(output_file, 'w') as file:
    sys.stdout = file  

    print("Longest Common Subsequence is", build_lcs(
        build_lcs_matrix(str1, str2)[0],
        build_lcs_matrix(str1, str2)[1],
        build_lcs_matrix(str1, str2)[2],
    ))

    sys.stdout = sys.__stdout__  # Reset the standard output

print("Result written to", output_file)
