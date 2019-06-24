
#Uses xmacrorec2 to record and then store a macro.
#Uses 'sgs', a private program to store text strings by tag. 
# sgs is not available right now but this specific functionality is easy to replicate yourself.

#prepare variables
datapath=~/programs/macros/_data
macropath=~/programs/macros/test_macro

#remove modifiers to avoid pain
cp ~/programs/macros/prepare_macro $macropath
echo "" >> $macropath

#get macro from user
xmacrorec2 >> $macropath

echo "" >> $macropath
echo "MotionNotify 600 600" >> $macropath

# add macro to sgs's database
cat $macropath | sgs +macro
data_value=$(cat $datapath)

#clear macro tag
sgs +$data_value -m "junk"
yes | sgs $data_value --

# set micro to specific tag 
cat $macropath | sgs +$data_value +macro
