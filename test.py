import numpy as np
import xlsxwriter

t0 = 0
s0 = 0
v0 = 98.1
t_end = 20
h = 0.05
g = -9.81
t_values = np.arange(t0, t_end + h, h)
s_values = []
v_values = []
s = s0
v = v0
for t in t_values:
    s_values.append(s)
    v_values.append(v)
    k1s = h * v
    k1v = h * g
    k2s = h * (v + 0.5 * k1v)
    k2v = h * g
    k3s = h * (v + 0.5 * k2v)
    k3v = h * g
    k4s = h * (v + k3v)
    k4v = h * g
    s += (k1s + 2 * k2s + 2 * k3s + k4s) / 6
    v += (k1v + 2 * k2v + 2 * k3v + k4v) / 6

analytical_s = 0.5 * g * t_values**2 + v0 * t_values
analytical_v = g * t_values + v0
workbook = xlsxwriter.Workbook('XOXO.xlsx')
worksheet = workbook.add_worksheet('sheet')
row = 1
worksheet.write(0,0,'t')
worksheet.write(0,1,'Numerical s(t)')
worksheet.write(0,2,'Analytical s(t)')
worksheet.write(0,3,'Numerical v(t)')
worksheet.write(0,4,'Analytical v(t)')
for i, t in enumerate(t_values):
	worksheet.write(row,0,t)
	worksheet.write(row,1,s_values[i])
	worksheet.write(row,2,analytical_s[i])
	worksheet.write(row,3,v_values[i])
	worksheet.write(row,4,analytical_v[i])
	print(f"t = {t:.2f}, Numerical s(t) = {s_values[i]:.4f}, Analytical s(t) = {analytical_s[i]:.4f}, Numerical v(t) = {v_values[i]:.4f}, Analytical v(t) = {analytical_v[i]:.4f}")
	row += 1
workbook.close()

