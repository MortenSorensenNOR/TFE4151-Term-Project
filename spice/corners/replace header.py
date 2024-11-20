


def replace_first_line(file_path, new_line):
    # Read all lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Replace the first line with the new one
    lines[0] = new_line + '\n'

    # Write back the modified lines to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)


corners = ["tt", "ff", "ss", "fs", "sf"]
neg20   = ["export 2/" + s + "-20" for s in corners]
plus27   = ["export 2/" + s + "27" for s in corners]
plus50   = ["export 2/" + s + "50" for s in corners]
new_line = 'time	time	v(vdd)	v(rw)	v(wordline)	v(i)	v(bitcarry)	v(t6)	v(1:t)	v(t1)	v(rwtemp)	v(t7)	v(2:t)	v(t4)	v(t8)	v(3:t)	v(t2)	v(iinv)	v(t9)	v(4:t)	v(t3)	v(5:t)	v(q)	v(qinv)	v(6:t)	v(7:yinv)	v(7:t)	v(t5)	v(8:t)	v(8:yinv)	v(bitout)	i(v_bitcarry)	i(v_i)	i(v_wordline)	i(v_rw)	i(v_vss)	i(v_vdd)'

for corner in neg20:
    replace_first_line(corner, new_line)
    
for corner in plus27:
    replace_first_line(corner, new_line)

for corner in plus50:
    replace_first_line(corner, new_line)
