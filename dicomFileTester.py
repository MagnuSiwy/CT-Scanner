from pydicom import dataset, dcmread, sequence
import matplotlib.pyplot as plt
import numpy as np

dicomFile = dcmread("test.dcm")

dataset.validate_file_meta(dicomFile.file_meta)
sequence.validate_dataset(dicomFile)

print(dicomFile)
# print(np.max(dicomFile.pixel_array))

fig, ax = plt.subplots()
ax = plt.imshow(dicomFile.pixel_array, cmap='gray')
plt.show()