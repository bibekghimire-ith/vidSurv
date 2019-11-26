from login import db, Image

# db.create_all()

pic1 = Image('proj.jpg')
pic2 = Image('project2.jpg')
pic3 = Image('progicon.jpg')

# print(pic2.id)
# print(pic1.name)


# db.session.add(pic1)
# db.session.add_all([pic1, pic2, pic3])

# db.session.commit()

# print(pic2.id)
# print(pic1.name)

# images = Image.query.all()
# for image in images:
#     print(image.name)

snaps = Image.query.order_by(Image.id.desc()).all()
# snaps = images.order_by(images.id.desc())

for snap in snaps:
    print(snap.id)
