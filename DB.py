import csv
with open('customers.csv','r+') as csvfile_1:# Load customers.csv
 with open('orders.csv','r+') as csvfile_2:# Load orders.csv
     def Find_Customer():#Find Operation
         reader = csv.DictReader(csvfile_1)
         print('Please enter the key and the value,enter # to finish')
         cal = 0
         l_1 = []
         l_2 = []
         while input()!='#':
              global cal,l_1,l_2
              l_1[cal] = input('Key_{}:',format(cal))
              l_2[cal] = input('Value_{}:',format(cal))
              cal = cal+1
         print('Enter Finished')#Let user enter the term that use to find the information
         cal_t = 0
         for row in reader:
              cal_2 = 0
              for x in range(cal):
                   if row['l_1[x]']==l_2[x]:
                        global cal_2
                        cal_2 = cal_2+1
              if (cal_2-cal)==1:
                   print(row)
                   global cal_t
                   cal_t = cal_t+1
         if cal_t == 0:
              print('Did not find this customer')   
     def Insert_Customer():#Insert Operation
         reader = csv.DictReader(csvfile_1)
         writer = csv.writer(csvfile_1)
         for i,rows in enumerate(reader):#Get the key of the table
              if i == 1:
                   row = rows
         cal_3 = row.keys().len();
         new_row = []
         print('Please enter the information of Customer')
         for x in cal_3:
               new_row[x] = input('{}:',format(row.keys()[x]))
         print('The content you want to insert is : /n{}',format(new_row))
         writer.writerow(new_row)
     def Find_Order():#Find Operation
         reader = csv.DictReader(csvfile_2)
         print('Please enter the key and the value,enter # to finish')
         cal_5 = 0
         l_3 = []
         l_4 = []
         while input()!='#':
              global cal_5,l_3,l_4
              l_3[cal_5] = input('Key_{}:',format(cal_5))
              l_4[cal_5] = input('Value_{}:',format(cal_5))
              cal_5 = cal_5+1
         print('Enter Finished')#Let user enter the term that use to find the information
         cal_tt = 0
         for row in reader:
              cal_6 = 0
              for x in range(cal_5):
                   if row['l_3[x]']==l_4[x]:
                        global cal_6
                        cal_6 = cal_6+1
              if (cal_6-cal_5)==1:
                   print(row)
                   global cal_tt
                   cal_tt = cal_tt+1
         if cal_tt == 0:
              print('Did not find this customer')
     def Insert_Order():#Insert Operation
         reader = csv.DictReader(csvfile_2)
         writer = csv.writer(csvfile_2)
         for i,rows in enumerate(reader):#Get the key of the table
              if i == 1:
                   row = rows
         cal_7 = row.keys().len();
         new_row = []
         print('Please enter the information of Customer')
         for x in cal_7:
              new_row[x] = input('{}:',format(row.keys()[x]))
         print('The content you want to insert is : /n{}',format(new_row))
         writer.writerow(new_row)
     def main():
         print('CSV file loading successed.Feel free to Find or Insert./nEnter Exit to exit.')
         while input()!= 'Exit':
              if input() == 'Find Customer':
                   Find_Customer()
              elif input() == 'Insert Customer':
                   Insert_Customer()
              elif input() == 'Find Order':
                   Find_Order()
              elif input() == 'Insert Order':
                   Insert_Order()
              else:
                   print('False order!')
         exit()
if __name__ == '__main__':
    main()