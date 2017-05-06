import csv
import numpy

# https://physionet.org/challenge/2012/#weight
# used variables: 1. Age    2. Gender   3. Weight   4. GCS
#                 5. HR     6. DiasABP 7. RespRate 8. Temp
#                 9. Urine  10. HCT     11. BUN     12. Glucose
#                 13. HCO3  14. K       15. Na      16. WBC
#                 17. DiasABP   18.MechVent 19. outcome


# function to parse one input file
def parse_file(input_fileName, output_fileName, SAP, SOFA, outcome):
    # initialize variables
    Age     = 0;        Gender   = 0;        Weight   = 0;        GCS = 0;
    variables = ['HR',  'SysABP', 'RespRate', 'Temp',
                 'Urine', 'HCT', 'BUN', 'Glucose',
                 'HCO3', 'K', 'Na', 'WBC',
                 'DiasABP']
           
    readings = [[] for ii in range(0, len(variables)*2)]


    # read everything into the arrays
    with open(input_fileName, 'r') as input_file:
        input_reader = csv.reader(input_file, delimiter = ',')
        next(input_reader); next(input_reader);
        # check for static variables
        for row in input_reader:
            if ((row[1] == 'ICUType') & (row[2] != '2')):
                return;
            
            if (row[1] == 'Age'):
                Age = row[2]

            if (row[1] == 'Gender'):
                Gender = row[2]

            if (row[1] == 'Weight'):
                Weight = row[2]

            # manual discretize (3 groups)
            if (row[1] == 'GCS'):
                GCS = int(row[2])
            #    if (GCS < 8):
            #        GCS = 0
            #    elif (GCS < 11):
            #        GCS = 1
            #    else:
            #        GCS = 2
            
            if row[1] in variables:
                if (int(row[0].split(':')[0]) < 24):
                    readings[variables.index(row[1])*2].append(float(row[2]))
                else:
                    readings[variables.index(row[1])*2+1].append(float(row[2]))
                    
    input_file.close()

    # post-processing and writing the results to file
    output_file = open(output_fileName, 'a+')

    # write static variables
    output_file.write('%s\t' %Age)
    output_file.write('%s\t' %Gender)
    output_file.write('%s\t' %Weight)
    output_file.write('%s\t' %GCS)

    # write dynamic variables after computing their feature values (mean, min, max)
    for ii in range(0, len(readings)):
        if (len(readings[ii]) > 0):
            #output_file.write('%f\t' %numpy.mean(readings[ii]))
            output_file.write('%f\t' %numpy.min(readings[ii]))
            #output_file.write('%f\t' %numpy.max(readings[ii]))
        else:
            output_file.write('-1\t')
            #output_file.write('-1\t')
            #output_file.write('-1\t')

    # manual discretization (3 groups)
    #if (SAP < 10):
    #    output_file.write('0\t')
    #elif (SAP < 20):
    #    output_file.write('1\t')
    #else:
    #    output_file.write('2\t')
    #
    #if (SOFA < 5):
    #    output_file.write('0\t')
    #elif (SOFA < 10):
    #    output_file.write('1\t')
    #else:
    #    output_file.write('2\t')
    #
    output_file.write('%s\t' %SAP)
    output_file.write('%s\t' %SOFA)

    if (outcome == '0'):
        output_file.write('survived\n')
    else:
        output_file.write('dead\n')
    
    
            
# loop through all files
output_fileName  =  'output.txt'
outcome_fileName = 'Outcomes-a.txt'
data_folder      = '.\set-a\\'

variables = ['HR',  'SysABP', 'RespRate', 'Temp',
             'Urine', 'HCT', 'BUN', 'Glucose',
             'HCO3', 'K', 'Na', 'WBC',
             'DiasABP']

output_file = open(output_fileName, 'w+')

# write down the first row of the output file
output_file.write('Age\tGender\tWeight\tGCS\t')
for ii in range(0, len(variables)):
    output_file.write('%s\t%s\t' %(variables[ii] + '_1', variables[ii] + '_2'))
output_file.write('SAP-I\t')
output_file.write('SOFA\t')
output_file.write('outcome,class(survived,dead)\n')
output_file.close()

# read outcome file
with open(outcome_fileName, 'r') as outcome_file:
    reader = csv.reader(outcome_file, delimiter = ',')
    # skip first line
    next(reader);
    counter = 0
    for row in reader:
        if (counter < 1500):
            parse_file(data_folder + row[0] + '.txt', output_fileName, int(row[1]), int(row[2]), row[5])
            counter = counter + 1
outcome_file.close()
