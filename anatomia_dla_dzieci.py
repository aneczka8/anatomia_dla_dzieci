from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * #QBrush, QPainter, QPen, QPixmap, QPolygonF
import sys
import pygame

app = QApplication(sys.argv)

def set_body_part_visible(a, b, c, d, e, f):
    boy_front_picture_item.setVisible(a)
    girl_front_picture_item.setVisible(b)
    boy_back_picture_item.setVisible(c)
    girl_back_picture_item.setVisible(d)
    boy_head_picture_item.setVisible(e)
    girl_head_picture_item.setVisible(f)

class MyGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.zoomed_in = False
        self.active_scene = scene_all
    
    def mousePressEvent(self, event):
        ### ADD BODY PARTS SOUNDS ###
        pos = self.mapToScene(event.pos())

        ankle_pos = ankle.mapFromScene(pos)
        ankle1_back_pos = ankle1_back.mapFromScene(pos)
        ankle2_back_pos = ankle2_back.mapFromScene(pos)
        arm1_pos = arm1.mapFromScene(pos)
        arm2_pos = arm2.mapFromScene(pos)
        arm1_back_pos = arm1_back.mapFromScene(pos)
        arm2_back_pos = arm2_back.mapFromScene(pos)
        back_pos = back.mapFromScene(pos)
        belly_pos = belly.mapFromScene(pos)
        buttock_pos = buttock.mapFromScene(pos)
        calf1_pos = calf1.mapFromScene(pos)
        calf2_pos = calf2.mapFromScene(pos)
        calf1_back_pos = calf1_back.mapFromScene(pos)
        calf2_back_pos = calf2_back.mapFromScene(pos)
        cheek1_pos = cheek1.mapFromScene(pos)
        cheek2_pos = cheek2.mapFromScene(pos)
        chest_pos = chest.mapFromScene(pos)
        chin_pos = chin.mapFromScene(pos)
        cleavage_pos = cleavage.mapFromScene(pos)
        ear_pos = ear.mapFromScene(pos)
        elbow1_pos = elbow1.mapFromScene(pos)
        elbow2_pos = elbow2.mapFromScene(pos)
        elbow1_back_pos = elbow1_back.mapFromScene(pos)
        elbow2_back_pos = elbow2_back.mapFromScene(pos)
        eye_pos = eye.mapFromScene(pos)   
        eyebrow1_pos = eyebrow1.mapFromScene(pos)
        eyebrow2_pos = eyebrow2.mapFromScene(pos)
        eyelid_pos = eyelid.mapFromScene(pos)
        finger1_pos = finger1.mapFromScene(pos)
        finger2_pos = finger2.mapFromScene(pos)
        finger1_back_pos = finger1_back.mapFromScene(pos)
        finger2_back_pos = finger2_back.mapFromScene(pos)
        foot1_pos = foot1.mapFromScene(pos)
        foot2_pos = foot2.mapFromScene(pos)
        foot_back_pos = foot_back.mapFromScene(pos)
        forearm1_pos = forearm1.mapFromScene(pos)
        forearm2_pos = forearm2.mapFromScene(pos)
        forearm1_back_pos = forearm1_back.mapFromScene(pos)
        forearm2_back_pos = forearm2_back.mapFromScene(pos)
        forehead_boy_pos = forehead_boy.mapFromScene(pos)
        forehead_girl_pos = forehead_girl.mapFromScene(pos)
        hair_boy_pos = hair_boy.mapFromScene(pos)
        hair_girl_pos = hair_girl.mapFromScene(pos)
        hair_girl_back_pos = hair_girl_back.mapFromScene(pos)
        hand_pos = hand.mapFromScene(pos)
        hand_back_pos = hand_back.mapFromScene(pos)
        head_boy_pos = head_boy.mapFromScene(pos)
        head_girl_pos = head_girl.mapFromScene(pos)
        head1_back_pos = head1_back.mapFromScene(pos)
        head2_back_pos = head2_back.mapFromScene(pos)
        heel_pos = heel.mapFromScene(pos)
        heel1_back_pos = heel1_back.mapFromScene(pos)
        heel2_back_pos = heel2_back.mapFromScene(pos)
        hip1_pos = hip1.mapFromScene(pos)
        hip2_pos = hip2.mapFromScene(pos)
        knee1_pos = knee1.mapFromScene(pos)
        knee2_pos = knee2.mapFromScene(pos)
        lashes_pos = lashes.mapFromScene(pos)
        lips_pos = lips.mapFromScene(pos)
        nape_pos = nape.mapFromScene(pos)
        neck_pos = neck.mapFromScene(pos)
        nose_pos = nose.mapFromScene(pos)
        palm_pos = palm.mapFromScene(pos)
        palm_back_pos = palm_back.mapFromScene(pos)
        penis_pos = penis.mapFromScene(pos)
        scrotum_pos = scrotum.mapFromScene(pos)
        shoulder1_pos = shoulder1.mapFromScene(pos)
        shoulder2_pos = shoulder2.mapFromScene(pos)
        shoulder1_back_pos = shoulder1_back.mapFromScene(pos)
        shoulder2_back_pos = shoulder2_back.mapFromScene(pos)
        temple_pos = temple.mapFromScene(pos)
        thigh1_pos = thigh1.mapFromScene(pos)
        thigh2_pos = thigh2.mapFromScene(pos)
        thigh1_back_pos = thigh1_back.mapFromScene(pos)
        thigh2_back_pos = thigh2_back.mapFromScene(pos)
        toe1_pos = toe1.mapFromScene(pos)
        toe2_pos = toe2.mapFromScene(pos)
        toe_back_pos = toe_back.mapFromScene(pos)
        vulva_pos = vulva.mapFromScene(pos)
        wrist1_pos = wrist1.mapFromScene(pos)
        wrist2_pos = wrist2.mapFromScene(pos)
        wrist1_back_pos = wrist1_back.mapFromScene(pos)
        wrist2_back_pos = wrist2_back.mapFromScene(pos)

        if self.active_scene == scene_boy_head or self.active_scene == scene_girl_head:
            if eye.contains(eye_pos):
                eye_sound.play()

            elif eyelid.contains(eyelid_pos):
                eyelid_sound.play()

            elif nose.contains(nose_pos):
                nose_sound.play()

            elif eyebrow1.contains(eyebrow1_pos) or eyebrow2.contains(eyebrow2_pos):
                eyebrow_sound.play()

            elif lashes.contains(lashes_pos):
                lashes_sound.play()

            elif lips.contains(lips_pos):
                lips_sound.play()

            elif cheek1.contains(cheek1_pos) or cheek2.contains(cheek2_pos):
                cheek_sound.play()

            elif ear.contains(ear_pos):
                ear_sound.play()

            elif temple.contains(temple_pos):
                temple_sound.play()

            elif chin.contains(chin_pos):
                chin_sound.play()

        if self.active_scene == scene_boy_head:
            if hair_boy.contains(hair_boy_pos):
                hair_sound.play()

            elif forehead_boy.contains(forehead_boy_pos):
                forehead_sound.play()

        if self.active_scene == scene_girl_head:
            if forehead_girl.contains(forehead_girl_pos):
                forehead_sound.play()

            elif hair_girl.contains(hair_girl_pos):
                hair_sound.play()

        if self.active_scene == scene_boy_front or self.active_scene == scene_girl_front: 
            if neck.contains(neck_pos):
                neck_sound.play() 

            elif cleavage.contains(cleavage_pos):
                cleavage_sound.play()

            elif chest.contains(chest_pos):
                chest_sound.play()

            elif belly.contains(belly_pos):
                belly_sound.play()

            elif shoulder1.contains(shoulder1_pos) or shoulder2.contains(shoulder2_pos):
                shoulder_sound.play()

            elif arm1.contains(arm1_pos) or arm2.contains(arm2_pos):
                arm_sound.play()

            elif elbow1.contains(elbow1_pos) or elbow2.contains(elbow2_pos):
                elbow_sound.play()

            elif forearm1.contains(forearm1_pos) or forearm2.contains(forearm2_pos):
                forearm_sound.play()

            elif wrist1.contains(wrist1_pos) or wrist2.contains(wrist2_pos):
                wrist_sound.play()

            elif palm.contains(palm_pos):
                palm_sound.play()

            elif finger1.contains(finger1_pos) or finger2.contains(finger2_pos) or toe1.contains(toe1_pos) or toe2.contains(toe2_pos):
                finger_sound.play()

            elif hand.contains(hand_pos):
                hand_sound.play()

            elif hip1.contains(hip1_pos) or hip2.contains(hip2_pos):
                hip_sound.play()

            elif thigh1.contains(thigh1_pos) or thigh2.contains(thigh2_pos):
                thigh_sound.play()
            
            elif knee1.contains(knee1_pos) or knee2.contains(knee2_pos):
                knee_sound.play()

            elif calf1.contains(calf1_pos) or calf2.contains(calf2_pos):
                calf_sound.play()

            elif heel.contains(heel_pos):
                heel_sound.play()

            elif foot1.contains(foot1_pos) or foot2.contains(foot2_pos):
                foot_sound.play()

            elif ankle.contains(ankle_pos):
                ankle_sound.play()
        
        if self.active_scene == scene_boy_front:
            if penis.contains(penis_pos):
                penis_sound.play()

            elif scrotum.contains(scrotum_pos):
                scrotum_sound.play()

            elif head_boy.contains(head_boy_pos):
                head_sound.play()

        if self.active_scene == scene_girl_front:
            if vulva.contains(vulva_pos):
                vulva_sound.play()

            elif head_girl.contains(head_girl_pos):
                head_sound.play()

        if self.active_scene == scene_boy_back or self.active_scene == scene_girl_back:
            if head1_back.contains(head1_back_pos) or head2_back.contains(head2_back_pos):
                head_sound.play()

            elif nape.contains(nape_pos):
                nape_sound.play()

            elif finger1_back.contains(finger1_back_pos):
                finger_sound.play()

            elif hand_back.contains(hand_back_pos):
                hand_sound.play()

            elif shoulder1_back.contains(shoulder1_back_pos) or shoulder2_back.contains(shoulder2_back_pos):
                shoulder_sound.play()

            elif arm1_back.contains(arm1_back_pos) or arm2_back.contains(arm2_back_pos):
                arm_sound.play()

            elif elbow1_back.contains(elbow1_back_pos) or elbow2_back.contains(elbow2_back_pos):
                elbow_sound.play()

            elif forearm1_back.contains(forearm1_back_pos) or forearm2_back.contains(forearm2_back_pos):
                forearm_sound.play()

            elif wrist1_back.contains(wrist1_back_pos) or wrist2_back.contains(wrist2_back_pos):
                wrist_sound.play()

            elif palm_back.contains(palm_back_pos):
                palm_sound.play()

            elif finger1_back.contains(finger1_back_pos) or finger2_back.contains(finger2_back_pos):
                finger_sound.play()

            elif back.contains(back_pos):
                back_sound.play()

            elif buttock.contains(buttock_pos):
                buttock_sound.play()

            elif thigh1_back.contains(thigh1_back_pos) or thigh2_back.contains(thigh2_back_pos):
                thigh_sound.play()

            elif calf1_back.contains(calf1_back_pos) or calf2_back.contains(calf2_back_pos):
                calf_sound.play()

            elif heel1_back.contains(heel1_back_pos) or heel2_back.contains(heel2_back_pos):
                heel_sound.play()

            elif foot_back.contains(foot_back_pos):
                foot_sound.play()

            elif toe_back.contains(toe_back_pos):
                finger_sound.play()

            elif ankle1_back.contains(ankle1_back_pos) or ankle2_back.contains(ankle2_back_pos):
                ankle_sound.play()

        if self.active_scene == scene_girl_back:
            if hair_girl_back.contains(hair_girl_back_pos):
                hair_sound.play()


    def mouseDoubleClickEvent(self, event):
    ### CHOOSE PICTURE ###
        pos = self.mapToScene(event.pos())

        boy_front_pos = boy_front.mapFromScene(pos)
        girl_front_pos = girl_front.mapFromScene(pos)
        boy_back_pos = boy_back.mapFromScene(pos)
        girl_back_pos = girl_back.mapFromScene(pos)
        boy_head_pos = boy_head.mapFromScene(pos)
        girl_head_pos = girl_head.mapFromScene(pos)

        if not self.zoomed_in:
            self.zoomed_in = True
            if boy_front.contains(boy_front_pos):
                set_body_part_visible(True, False, False, False, False, False)
                self.setScene(scene_boy_front)
                self.active_scene = scene_boy_front
            elif girl_front.contains(girl_front_pos):
                set_body_part_visible(False, True, False, False, False, False)
                self.setScene(scene_girl_front)
                self.active_scene = scene_girl_front
            elif boy_back.contains(boy_back_pos):
                set_body_part_visible(False, False, True, False, False, False)
                self.setScene(scene_boy_back)
                self.active_scene = scene_boy_back
            elif girl_back.contains(girl_back_pos):
                set_body_part_visible(False, False, False, True, False, False)
                self.setScene(scene_girl_back)
                self.active_scene = scene_girl_back
            elif boy_head.contains(boy_head_pos):
                set_body_part_visible(False, False, False, False, True, False)
                self.setScene(scene_boy_head)
                self.active_scene = scene_boy_head
            elif girl_head.contains(girl_head_pos):
                set_body_part_visible(False, False, False, False, False, True)
                self.setScene(scene_girl_head)
                self.active_scene = scene_girl_head

        else:
            self.setScene(scene_all)
            self.zoomed_in = False
            self.active_scene = scene_all

##### SCENE WITH ONE PICTURE AT A TIME ###### 
              
scene_boy_front = QGraphicsScene(0, 0, 450, 750)
scene_boy_back = QGraphicsScene(0, 0, 450, 750)
scene_boy_head = QGraphicsScene(0, 0, 450, 750)
scene_girl_front = QGraphicsScene(0, 0, 450, 750)
scene_girl_back = QGraphicsScene(0, 0, 450, 750)
scene_girl_head = QGraphicsScene(0, 0, 450, 750)

boy_front_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/boy_front.jpeg").scaledToHeight(700,mode=Qt.SmoothTransformation)
boy_front_picture_item = scene_boy_front.addPixmap(boy_front_picture)
girl_front_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/girl_front.jpeg").scaledToHeight(700,mode=Qt.SmoothTransformation)
girl_front_picture_item = scene_girl_front.addPixmap(girl_front_picture)

boy_back_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/boy_back.jpeg").scaledToHeight(700,mode=Qt.SmoothTransformation)
boy_back_picture_item = scene_boy_back.addPixmap(boy_back_picture)
girl_back_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/girl_back.jpeg").scaledToHeight(700,mode=Qt.SmoothTransformation)
girl_back_picture_item = scene_girl_back.addPixmap(girl_back_picture)

boy_head_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/boy_head.jpeg").scaledToWidth(700,mode=Qt.SmoothTransformation)
boy_head_picture_item = scene_boy_head.addPixmap(boy_head_picture)
boy_head_picture_item.moveBy(-80,0)
girl_head_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/girl_head.jpeg").scaledToWidth(700,mode=Qt.SmoothTransformation)
girl_head_picture_item = scene_girl_head.addPixmap(girl_head_picture)
girl_head_picture_item.moveBy(-80,0)

girl_head_picture_item.setVisible(False)
boy_head_picture_item.setVisible(False)
girl_front_picture_item.setVisible(False)
boy_front_picture_item.setVisible(False)
girl_back_picture_item.setVisible(False)
boy_back_picture_item.setVisible(False)

pen = QPen(Qt.green)
pen.setStyle(Qt.NoPen)

eye_path = QPainterPath()
eye_path.moveTo(160*1.8-80, 145*1.8+40)
eye_path.cubicTo(170*1.8-80, 115*1.8+40, 190*1.8-80, 115*1.8+40, 200*1.8-80, 145*1.8+40)
eye_path.cubicTo(190*1.8-80, 155*1.8+40, 170*1.8-80, 155*1.8+40, 160*1.8-80, 145*1.8+40)
eye = QGraphicsPathItem(eye_path)
eye.setPen(pen)
eyeitem = scene_boy_head.addItem(eye)

eyelid_path = QPainterPath()
eyelid_path.moveTo(332, 297)
eyelid_path.cubicTo(225*1.8-80, 112*1.8+40, 249*1.8-80, 115*1.8+40, 384, 290)
eyelid_path.cubicTo(347, 308, 350, 297, 332, 297)
eyelid = QGraphicsPathItem(eyelid_path)
eyelid.setPen(pen)
eyeliditem = scene_boy_head.addItem(eyelid)

nose_path = QPainterPath()
nose_path.moveTo(212*1.8-80, 141*1.8+40)
nose_path.cubicTo(215*1.8-75, 150*1.8+40, 207*1.8-77, 145*1.8+40, 223*1.8-78, 155*1.8+40)
nose_path.cubicTo(218*1.8-67, 163*1.8+45, 215*1.8-90, 163*1.8+40, 210*1.8-80, 160*1.8+43)
nose = QGraphicsPathItem(nose_path)
nose.setPen(pen)
noseitem = scene_boy_head.addItem(nose)

eyebrow1_path = QPainterPath()
eyebrow1_path.moveTo(168*1.8-80, 115*1.8+40)
eyebrow1_path.cubicTo(180*1.8-80, 107*1.8+40, 175*1.8-80, 106*1.8+40, 190*1.8-80, 109*1.8+40)
eyebrow1_path.lineTo(190*1.8-80, 111*1.8+40)
eyebrow1_path.cubicTo(170*1.8-80, 112*1.8+40, 185*1.8-80, 111*1.8+40, 168*1.8-80, 118*1.8+40)
eyebrow1_path.lineTo(168*1.8-80, 115*1.8+40)
eyebrow1 = QGraphicsPathItem(eyebrow1_path)
eyebrow1.setPen(pen)
eyebrow1item = scene_boy_head.addItem(eyebrow1)

eyebrow2_path = QPainterPath()
eyebrow2_path.moveTo(234*1.8-80, 108*1.8+40)
eyebrow2_path.cubicTo(245*1.8-80, 108*1.8+40, 240*1.8-70, 106*1.8+40, 253*1.8-80, 117*1.8+40)
eyebrow2_path.lineTo(251*1.8-80, 118*1.8+40)
eyebrow2_path.cubicTo(245*1.8-80, 109*1.8+40, 234*1.8-80, 110*1.8+40, 234*1.8-80, 110*1.8+42)
eyebrow2_path.lineTo(234*1.8-80, 108*1.8+40)
eyebrow2 = QGraphicsPathItem(eyebrow2_path)
eyebrow2.setPen(pen)
eyebrow2item = scene_boy_head.addItem(eyebrow2)

lashes_path = QPainterPath()
lashes_path.moveTo(155*1.8-80, 144*1.8+40)
lashes_path.cubicTo(166*1.8-80, 115*1.8+40, 156*1.8-80, 130*1.8+40, 173*1.8-80, 120*1.8+40)
lashes_path.lineTo(174*1.8-80, 122*1.8+40)
lashes_path.cubicTo(160*1.8-75, 135*1.8+40, 165*1.8-80, 125*1.8+40, 158*1.8-80, 145*1.8+40)
lashes = QGraphicsPathItem(lashes_path)
lashes.setPen(pen)
lashesitem = scene_boy_head.addItem(lashes)

lips_path = QPainterPath()
lips_path.moveTo(242, 348)
lips_path.cubicTo(310, 365, 310, 365, 342, 352)
lips_path.lineTo(344, 357)
lips_path.cubicTo(310, 370, 310, 370, 242, 355)
lips = QGraphicsPathItem(lips_path)
lips.setPen(pen)
lipsitem = scene_boy_head.addItem(lips)

cheek1 = QGraphicsEllipseItem()
cheek1.setRect(139+30,148+165,31*1.8,31*1.8)
cheek1.setPen(pen)
cheek1item = scene_boy_head.addItem(cheek1)

cheek2_path = QPainterPath()
cheek2_path.moveTo(250*1.8-80, 177*1.8+40)
cheek2_path.cubicTo(225*1.8-80, 180*1.8+40, 230*1.8-80, 135*1.8+40, 262*1.8-80, 155*1.8+40)
cheek2_path.cubicTo(260*1.8-80, 168*1.8+40, 261*1.8-80, 165*1.8+40, 250*1.8-80, 177*1.8+40)
cheek2 = QGraphicsPathItem(cheek2_path)
cheek2.setPen(pen)
cheek2item = scene_boy_head.addItem(cheek2)

ear_path = QPainterPath()
ear_path.moveTo(139*1.8-80, 163*1.8+40)
ear_path.cubicTo(110*1.8-80, 158*1.8+40, 106*1.8-80, 110*1.8+40, 134*1.8-80, 131*1.8+40)
ear = QGraphicsPathItem(ear_path)
ear.setPen(pen)
earitem = scene_boy_head.addItem(ear)

temple = QGraphicsEllipseItem()
temple.setRect(180,123+143,12*1.8,20*1.8)
temple.setPen(pen)
templeitem = scene_boy_head.addItem(temple)

chin_path = QPainterPath()
chin_path.moveTo(187*1.8-80, 203*1.8+40)
chin_path.lineTo(190*1.8-80, 195*1.8+40)
chin_path.lineTo(222*1.8-80, 195*1.8+40)
chin_path.lineTo(224*1.8-80, 200*1.8+40)
chin_path.cubicTo(213*1.8-80, 207*1.8+40, 205*1.8-80, 210*1.8+40, 187*1.8-80, 203*1.8+40)
chin = QGraphicsPathItem(chin_path)
chin.setPen(pen)
chinitem = scene_boy_head.addItem(chin)

neck_path = QPainterPath()
neck_path.moveTo(176, 203)
neck_path.lineTo(207, 209)
neck_path.lineTo(211, 207)
neck_path.lineTo(214, 220)
neck_path.lineTo(185, 224)
neck_path.lineTo(172, 218)
neck = QGraphicsPathItem(neck_path)
neck.setPen(pen)
neckitem = scene_boy_front.addItem(neck)

cleavage_path = QPainterPath()
cleavage_path.moveTo(162, 220)
cleavage_path.lineTo(172, 219)
cleavage_path.lineTo(185, 225)
cleavage_path.lineTo(214, 221)
cleavage_path.lineTo(229, 228)
cleavage_path.cubicTo(197, 270, 160, 260, 162, 220)
cleavage = QGraphicsPathItem(cleavage_path)
cleavage.setPen(pen)
cleavageitem = scene_boy_front.addItem(cleavage)

chest_path = QPainterPath()
chest_path.moveTo(138, 261)
chest_path.cubicTo(185, 253, 195, 256, 229, 260)
chest_path.cubicTo(232, 290, 230, 285, 245, 310)
chest_path.cubicTo(195, 320, 170, 320, 136, 313)
chest_path.cubicTo(136, 280, 128, 281, 138, 261)
chest = QGraphicsPathItem(chest_path)
chest.setPen(pen)
chestitem = scene_boy_front.addItem(chest)

belly_path = QPainterPath()
belly_path.moveTo(165, 319)
belly_path.cubicTo(180, 320, 180, 321, 205, 318)
belly_path.cubicTo(324, 450, 30, 440, 165, 319)
belly = QGraphicsPathItem(belly_path)
belly.setPen(pen)
bellyitem = scene_boy_front.addItem(belly)

penis_path = QPainterPath()
penis_path.moveTo(175, 420)
penis_path.lineTo(165, 435)
penis_path.cubicTo(160, 445, 169, 443, 178, 440)
penis_path.lineTo(186, 430)
penis = QGraphicsPathItem(penis_path)
penis.setPen(pen)
penisitem = scene_boy_front.addItem(penis)

scrotum_path = QPainterPath()
scrotum_path.moveTo(187, 430)
scrotum_path.lineTo(193, 428)
scrotum_path.cubicTo(196, 445, 200, 440, 178, 444)
scrotum = QGraphicsPathItem(scrotum_path)
scrotum.setPen(pen)
scrotumitem = scene_boy_front.addItem(scrotum)

vulva_path = QPainterPath()
vulva_path.moveTo(166, 438)
vulva_path.cubicTo(186, 452, 191, 444, 197, 438)
vulva_path.cubicTo(186, 432, 180, 430, 166, 438)
vulva = QGraphicsPathItem(vulva_path)
vulva.setPen(pen)
vulvaitem = scene_girl_front.addItem(vulva)

shoulder1_path = QPainterPath()
shoulder1_path.moveTo(229, 260)
shoulder1_path.lineTo(239, 231)
shoulder1_path.cubicTo(242, 232, 249, 232, 266, 253)
shoulder1 = QGraphicsPathItem(shoulder1_path)
shoulder1.setPen(pen)
shoulder1item = scene_boy_front.addItem(shoulder1)

arm1_path = QPainterPath()
arm1_path.moveTo(266, 253)
arm1_path.cubicTo(245, 277, 245, 277, 245, 310)
arm1_path.lineTo(290, 343)
arm1_path.cubicTo(285, 318, 285, 318, 290, 301)
arm1 = QGraphicsPathItem(arm1_path)
arm1.setPen(pen)
arm1item = scene_boy_front.addItem(arm1)

elbow1_path = QPainterPath()
elbow1_path.moveTo(289, 316)
elbow1_path.lineTo(291, 344)
elbow1_path.cubicTo(308, 356, 310, 351, 318, 344)
elbow1 = QGraphicsPathItem(elbow1_path)
elbow1.setPen(pen)
elbow1item = scene_boy_front.addItem(elbow1)

forearm1_path = QPainterPath()
forearm1_path.moveTo(319, 343)
forearm1_path.cubicTo(335, 331, 331, 317, 336, 296)
forearm1_path.cubicTo(324, 296, 320, 294, 305, 284)
forearm1_path.lineTo(289, 315)
forearm1 = QGraphicsPathItem(forearm1_path)
forearm1.setPen(pen)
forearm1item = scene_boy_front.addItem(forearm1)

wrist1_path = QPainterPath()
wrist1_path.moveTo(305, 282)
wrist1_path.cubicTo(320, 292, 324, 294, 336, 294)
wrist1_path.lineTo(336, 289)
wrist1_path.cubicTo(326, 284, 322, 289, 309, 276)
wrist1 = QGraphicsPathItem(wrist1_path)
wrist1.setPen(pen)
wrist1item = scene_boy_front.addItem(wrist1)

palm_path = QPainterPath()
palm_path.moveTo(309, 275)
palm_path.cubicTo(311, 215, 387, 265, 336, 290)
palm = QGraphicsPathItem(palm_path)
palm.setPen(pen)
palmitem = scene_boy_front.addItem(palm)

finger1_path = QPainterPath()
finger1_path.moveTo(308, 275)
finger1_path.lineTo(302, 265)
finger1_path.lineTo(304, 231)
finger1_path.lineTo(307, 229)
finger1_path.lineTo(312, 232)
finger1_path.lineTo(312, 252)
finger1_path.lineTo(317, 248)
finger1_path.lineTo(332, 215)
finger1_path.lineTo(336, 218)
finger1_path.lineTo(330, 245)
finger1_path.lineTo(337, 242)
finger1_path.lineTo(350, 220)
finger1_path.lineTo(357, 222)
finger1_path.lineTo(345, 249)
finger1_path.lineTo(362, 236)
finger1_path.lineTo(367, 238)
finger1_path.lineTo(355, 257)
finger1_path.lineTo(370, 248)
finger1_path.lineTo(374, 254)
finger1_path.lineTo(357, 267)
finger1_path.cubicTo(339, 249, 313, 227, 308, 275)
finger1 = QGraphicsPathItem(finger1_path)
finger1.setPen(pen)
finger1item = scene_boy_front.addItem(finger1)

shoulder2_path = QPainterPath()
shoulder2_path.moveTo(138, 260)
shoulder2_path.lineTo(159, 220)
shoulder2_path.cubicTo(136, 227, 139, 221, 126, 245)
shoulder2 = QGraphicsPathItem(shoulder2_path)
shoulder2.setPen(pen)
shoulder2item = scene_boy_front.addItem(shoulder2)

arm2_path = QPainterPath()
arm2_path.moveTo(126, 246)
arm2_path.lineTo(101, 303)
arm2_path.lineTo(121, 331)
arm2_path.lineTo(132, 315)
arm2_path.lineTo(130, 276)
arm2_path.lineTo(137, 260)
arm2 = QGraphicsPathItem(arm2_path)
arm2.setPen(pen)
arm2item = scene_boy_front.addItem(arm2)

elbow2_path = QPainterPath()
elbow2_path.moveTo(101, 305)
elbow2_path.lineTo(121, 333)
elbow2_path.lineTo(91, 331)
elbow2 = QGraphicsPathItem(elbow2_path)
elbow2.setPen(pen)
elbow2item = scene_boy_front.addItem(elbow2)

forearm2_path = QPainterPath()
forearm2_path.moveTo(91, 333)
forearm2_path.lineTo(81, 383)
forearm2_path.cubicTo(94, 380, 91, 380, 105, 386)
forearm2_path.lineTo(116, 356)
forearm2_path.lineTo(119, 335)
forearm2 = QGraphicsPathItem(forearm2_path)
forearm2.setPen(pen)
forearm2item = scene_boy_front.addItem(forearm2)

wrist2_path = QPainterPath()
wrist2_path.moveTo(81, 385)
wrist2_path.cubicTo(94, 382, 91, 382, 105, 388)
wrist2_path.lineTo(102, 392)
wrist2_path.cubicTo(91, 389, 91, 390, 79, 400)
wrist2 = QGraphicsPathItem(wrist2_path)
wrist2.setPen(pen)
wrist2item = scene_boy_front.addItem(wrist2)

hand_path = QPainterPath()
hand_path.moveTo(102, 394)
hand_path.cubicTo(91, 391, 91, 392, 79, 402)
hand_path.lineTo(75, 416)
hand_path.lineTo(93, 418)
hand_path.lineTo(104, 407)
hand = QGraphicsPathItem(hand_path)
hand.setPen(pen)
handitem = scene_boy_front.addItem(hand)

finger2_path = QPainterPath()
finger2_path.moveTo(75, 418)
finger2_path.lineTo(74, 430)
finger2_path.lineTo(83, 449)
finger2_path.lineTo(95, 449)
finger2_path.lineTo(97, 443)
finger2_path.lineTo(90, 431)
finger2_path.lineTo(92, 421)
finger2_path.lineTo(105, 434)
finger2_path.lineTo(110, 429)
finger2_path.lineTo(104, 409)
finger2_path.lineTo(92, 420)
finger2 = QGraphicsPathItem(finger2_path)
finger2.setPen(pen)
finger2item = scene_boy_front.addItem(finger2)

hip1_path = QPainterPath()
hip1_path.moveTo(124, 407)
hip1_path.lineTo(125, 430)
hip1_path.lineTo(161, 435)
hip1_path.lineTo(170, 421)
hip1 = QGraphicsPathItem(hip1_path)
hip1.setPen(pen)
hip1item = scene_boy_front.addItem(hip1)

thigh1_path = QPainterPath()
thigh1_path.moveTo(125, 432)
thigh1_path.cubicTo(118, 460, 115, 470, 120, 507)
thigh1_path.lineTo(160, 522)
thigh1_path.lineTo(162, 507)
thigh1_path.lineTo(186, 455)
thigh1_path.lineTo(186, 446)
thigh1_path.cubicTo(168, 446, 160, 450, 161, 437)
thigh1 = QGraphicsPathItem(thigh1_path)
thigh1.setPen(pen)
thigh1item = scene_boy_front.addItem(thigh1)

knee1_path = QPainterPath()
knee1_path.moveTo(120, 509)
knee1_path.cubicTo(122, 514, 115, 518, 128, 532)
knee1_path.lineTo(160, 528)
knee1_path.lineTo(160, 525)
knee1 = QGraphicsPathItem(knee1_path)
knee1.setPen(pen)
knee1item = scene_boy_front.addItem(knee1)

calf1_path = QPainterPath()
calf1_path.moveTo(128, 534)
calf1_path.lineTo(120, 528)
calf1_path.lineTo(110, 620)
calf1_path.lineTo(142, 620)
calf1_path.cubicTo(160, 585, 168, 570, 160, 530)
calf1 = QGraphicsPathItem(calf1_path)
calf1.setPen(pen)
calf1item = scene_boy_front.addItem(calf1)

ankle = QGraphicsEllipseItem()
ankle.setRect(121,621,12,12)
ankle.setPen(pen)
ankleitem = scene_boy_front.addItem(ankle)

heel_path = QPainterPath()
heel_path.moveTo(136, 633)
heel_path.cubicTo(150, 648, 138, 664, 116, 656)
heel = QGraphicsPathItem(heel_path)
heel.setPen(pen)
heelitem = scene_boy_front.addItem(heel)

foot1_path = QPainterPath()
foot1_path.moveTo(114, 656)
foot1_path.lineTo(94, 661)
foot1_path.lineTo(84, 658)
foot1_path.lineTo(84, 649)
foot1_path.lineTo(102, 634)
foot1_path.lineTo(135, 636)
foot1 = QGraphicsPathItem(foot1_path)
foot1.setPen(pen)
foot1item = scene_boy_front.addItem(foot1)

toe1_path = QPainterPath()
toe1_path.moveTo(82, 658)
toe1_path.cubicTo(58, 664, 70, 640, 87, 646)
toe1_path.lineTo(82, 649)
toe1 = QGraphicsPathItem(toe1_path)
toe1.setPen(pen)
toe1item = scene_boy_front.addItem(toe1)

hip2_path = QPainterPath()
hip2_path.moveTo(195, 424)
hip2_path.lineTo(198, 438)
hip2_path.lineTo(245, 424)
hip2_path.lineTo(242, 400)
hip2 = QGraphicsPathItem(hip2_path)
hip2.setPen(pen)
hip2item = scene_boy_front.addItem(hip2)

thigh2_path = QPainterPath()
thigh2_path.moveTo(245, 426)
thigh2_path.lineTo(248, 510)
thigh2_path.cubicTo(235, 505, 218, 510, 215, 535)
thigh2_path.lineTo(188, 455)
thigh2_path.lineTo(188, 446)
thigh2_path.lineTo(195, 444)
thigh2_path.lineTo(197, 440)
thigh2 = QGraphicsPathItem(thigh2_path)
thigh2.setPen(pen)
thigh2item = scene_boy_front.addItem(thigh2)

knee2_path = QPainterPath()
knee2_path.moveTo(248, 512)
knee2_path.cubicTo(235, 507, 218, 512, 215, 535)
knee2_path.cubicTo(232, 537, 242, 539, 252, 524)
knee2 = QGraphicsPathItem(knee2_path)
knee2.setPen(pen)
knee2item = scene_boy_front.addItem(knee2)

calf2_path = QPainterPath()
calf2_path.moveTo(215, 539)
calf2_path.cubicTo(232, 541, 242, 543, 252, 528)
calf2_path.cubicTo(260, 545, 262, 580, 259, 625)
calf2_path.lineTo(238, 641)
calf2_path.cubicTo(205, 586, 223, 549, 215, 541)
calf2 = QGraphicsPathItem(calf2_path)
calf2.setPen(pen)
calf2item = scene_boy_front.addItem(calf2)

foot2_path = QPainterPath()
foot2_path.moveTo(238, 643)
foot2_path.lineTo(259, 627)
foot2_path.lineTo(277, 662)
foot2_path.lineTo(247, 676)
foot2_path.lineTo(238, 655)
foot2 = QGraphicsPathItem(foot2_path)
foot2.setPen(pen)
foot2item = scene_boy_front.addItem(foot2)

toe2_path = QPainterPath()
toe2_path.moveTo(277, 664)
toe2_path.cubicTo(272, 689, 245, 700, 247, 678)
toe2 = QGraphicsPathItem(toe2_path)
toe2.setPen(pen)
toe2item = scene_boy_front.addItem(toe2)

forehead_boy_path = QPainterPath()
forehead_boy_path.moveTo(272*1.8-80, 115*1.8+40)
forehead_boy_path.cubicTo(220*1.8-80, 100*1.8+40, 180*1.8-80, 104*1.8+40, 145*1.8-80, 114*1.8+40)
forehead_boy_path.lineTo(170*1.8-80, 91*1.8+40)
forehead_boy_path.lineTo(166*1.8-80, 106*1.8+40)
forehead_boy_path.lineTo(192*1.8-80, 95*1.8+40)
forehead_boy_path.lineTo(204*1.8-80, 78*1.8+40)
forehead_boy_path.lineTo(204*1.8-80, 93*1.8+40)
forehead_boy_path.cubicTo(222*1.8-80, 93*1.8+40, 234*1.8-80, 85*1.8+40, 244*1.8-80, 66*1.8+40)
forehead_boy_path.cubicTo(264*1.8-80, 76*1.8+40, 270*1.8-80, 104*1.8+40, 272*1.8-80, 115*1.8+40)
forehead_boy = QGraphicsPathItem(forehead_boy_path)
forehead_boy.setPen(pen)
forehead_boyitem = scene_boy_head.addItem(forehead_boy)

hair_boy_path = QPainterPath()
hair_boy_path.moveTo(145*1.8-80, 145*1.8+40)
hair_boy_path.cubicTo(138*1.8-80, 115*1.8+40, 150*1.8-80, 100*1.8+40, 171*1.8-80, 90*1.8+40)
hair_boy_path.lineTo(171*1.8-80, 90*1.8+40)
hair_boy_path.lineTo(166*1.8-80, 105*1.8+40)
hair_boy_path.lineTo(192*1.8-80, 94*1.8+40)
hair_boy_path.lineTo(204*1.8-80, 77*1.8+40)
hair_boy_path.lineTo(205*1.8-80, 91*1.8+40)
hair_boy_path.cubicTo(222*1.8-80, 91*1.8+40, 234*1.8-80, 83*1.8+40, 244*1.8-80, 64*1.8+40)
hair_boy_path.cubicTo(266*1.8-80, 76*1.8+40, 280*1.8-80, 104*1.8+40, 272*1.8-80, 143*1.8+40)
hair_boy_path.cubicTo(340*1.8-80, 105*1.8+40, 250*1.8-80, 5*1.8+40, 215*1.8-80, 8*1.8+40)
hair_boy_path.cubicTo(85*1.8-80, 0*1.8+40, 40*1.8-80, 155*1.8+40, 130*1.8-80, 170*1.8+40)
hair_boy_path.lineTo(130*1.8-80, 162*1.8+40)
hair_boy_path.cubicTo(109*1.8-80, 158*1.8+40, 104*1.8-80, 108*1.8+40, 134*1.8-80, 129*1.8+40)
hair_boy_path.lineTo(135*1.8-80, 141*1.8+40)
hair_boy = QGraphicsPathItem(hair_boy_path)
hair_boy.setPen(pen)
hair_boyitem = scene_boy_head.addItem(hair_boy)

head_boy_path = QPainterPath()
head_boy_path.moveTo(272, 146)
head_boy_path.cubicTo(340, 105, 250, 5, 215, 8)
head_boy_path.cubicTo(85, 0, 40, 155, 132, 170)
head_boy_path.cubicTo(157, 203, 170, 205, 210, 210)
head_boy_path.cubicTo(255, 190, 263, 170, 272, 146)
head_boy = QGraphicsPathItem(head_boy_path)
head_boy.setPen(pen)
head_boyitem = scene_boy_front.addItem(head_boy)

forehead_girl_path = QPainterPath()
forehead_girl_path.moveTo(260*1.8-80, 112*1.8+40)
forehead_girl_path.cubicTo(220*1.8-80, 100*1.8+40, 180*1.8-80, 104*1.8+40, 165*1.8-80, 110*1.8+40)
forehead_girl_path.cubicTo(190*1.8-80, 88*1.8+40, 211*1.8-80, 85*1.8+40, 220*1.8-80, 63*1.8+40)
forehead_girl_path.cubicTo(235*1.8-80, 83*1.8+40, 260*1.8-80, 94*1.8+40, 260*1.8-80, 112*1.8+40)
forehead_girl_path.moveTo(145*1.8-80, 115*1.8+40)
forehead_girl_path.cubicTo(150*1.8-80, 105*1.8+40, 150*1.8-80, 104*1.8+40, 168*1.8-80, 90*1.8+40)
forehead_girl_path.lineTo(160*1.8-80, 113*1.8+40)
forehead_girl = QGraphicsPathItem(forehead_girl_path)
forehead_girl.setPen(pen)
forehead_girlitem = scene_girl_head.addItem(forehead_girl)

hair_girl_path = QPainterPath()
hair_girl_path.moveTo(145*1.8-80, 145*1.8+40)
hair_girl_path.cubicTo(138*1.8-80, 115*1.8+40, 150*1.8-80, 100*1.8+40, 168*1.8-80, 89*1.8+40)
hair_girl_path.lineTo(161*1.8-80, 112*1.8+40)
hair_girl_path.cubicTo(190*1.8-80, 86*1.8+40, 211*1.8-80, 83*1.8+40, 220*1.8-80, 61*1.8+40)
hair_girl_path.cubicTo(235*1.8-80, 82*1.8+40, 260*1.8-80, 93*1.8+40, 265*1.8-80, 122*1.8+40)
hair_girl_path.lineTo(270*1.8-80, 109*1.8+40)
hair_girl_path.cubicTo(275*1.8-80, 142*1.8+40, 270*1.8-80, 150*1.8+40, 257*1.8-80, 175*1.8+40)
hair_girl_path.cubicTo(258*1.8-80, 285*1.8+40, 359*1.8-80, 163*1.8+40, 268*1.8-80, 152*1.8+40) #kitka
hair_girl_path.cubicTo(350*1.8-80, 105*1.8+40, 280*1.8-80, 0*1.8+40, 205*1.8-80, 13*1.8+40)
hair_girl_path.cubicTo(85*1.8-80, 0*1.8+40, 70*1.8-80, 135*1.8+40, 97*1.8-80, 152*1.8+40)
hair_girl_path.cubicTo(0*1.8-80, 170*1.8+40, 105*1.8-80, 290*1.8+40, 110*1.8-80, 165*1.8+40) #kitka
hair_girl_path.lineTo(140*1.8-80, 180*1.8+40)
hair_girl_path.lineTo(130*1.8-80, 162*1.8+40)
hair_girl_path.cubicTo(109*1.8-80, 158*1.8+40, 104*1.8-80, 108*1.8+40, 134*1.8-80, 129*1.8+40)
hair_girl_path.lineTo(135*1.8-80, 141*1.8+40)
hair_girl = QGraphicsPathItem(hair_girl_path)
hair_girl.setPen(pen)
hair_girlitem = scene_girl_head.addItem(hair_girl)

head_girl_path = QPainterPath()
head_girl_path.moveTo(257, 175)
head_girl_path.cubicTo(258, 285, 359, 163, 268, 152) #kitka
head_girl_path.cubicTo(350, 105, 280, 0, 205, 13)
head_girl_path.cubicTo(85, 0, 70, 135, 97, 152)
head_girl_path.cubicTo(0, 170, 105, 290, 110, 165) #kitka
head_girl_path.lineTo(140, 180)
head_girl_path.cubicTo(157, 203, 170, 205, 210, 210)
head_girl_path.cubicTo(255, 190, 250, 180, 257, 175)
head_girl = QGraphicsPathItem(head_girl_path)
head_girl.setPen(pen)
head_girlitem = scene_girl_front.addItem(head_girl)

head1_back = QGraphicsEllipseItem()
head1_back.setRect(85,8,200,200)
head1_back.setStartAngle(285*16)
head1_back.setSpanAngle(330*16)
head1_back.setPen(pen)
head1_backitem = scene_girl_back.addItem(head1_back)

head2_back_path = QPainterPath()
head2_back_path.moveTo(185,108)
head2_back_path.lineTo(158, 200)
head2_back_path.lineTo(195, 190)
head2_back_path.lineTo(210, 197)
head2_back = QGraphicsPathItem(head2_back_path)
head2_back.setPen(pen)
head2_backitem = scene_girl_back.addItem(head2_back)

hair_girl_back_path = QPainterPath()
hair_girl_back_path.moveTo(257, 177)
hair_girl_back_path.cubicTo(280, 270, 390, 183, 273, 152) #kitka
hair_girl_back_path.moveTo(100, 168)
hair_girl_back_path.cubicTo(55, 190, 100, 270, 137, 193) #kitka
hair_girl_back = QGraphicsPathItem(hair_girl_back_path)
hair_girl_back.setPen(pen)
hair_girl_backitem = scene_girl_back.addItem(hair_girl_back)

nape_path = QPainterPath()
nape_path.moveTo(162, 200)
nape_path.lineTo(195, 192)
nape_path.lineTo(208, 197)
nape_path.lineTo(208, 214)
nape_path.lineTo(158, 217)
nape = QGraphicsPathItem(nape_path)
nape.setPen(pen)
napeitem = scene_girl_back.addItem(nape)

finger1_back_path = QPainterPath()
finger1_back_path.moveTo(72, 275)
finger1_back_path.lineTo(78, 265)
finger1_back_path.lineTo(76, 231)
finger1_back_path.lineTo(73, 229)
finger1_back_path.lineTo(68, 232)
finger1_back_path.lineTo(68, 252) # koniec kciuka
finger1_back_path.lineTo(65, 248)
finger1_back_path.lineTo(50, 215)
finger1_back_path.lineTo(46, 218)
finger1_back_path.lineTo(52, 245) # koniec wskazującego
finger1_back_path.lineTo(46, 242)
finger1_back_path.lineTo(33, 220)
finger1_back_path.lineTo(27, 222)
finger1_back_path.lineTo(39, 249) # koniec środkowego
finger1_back_path.lineTo(22, 236)
finger1_back_path.lineTo(18, 238)
finger1_back_path.lineTo(32, 257)
finger1_back_path.lineTo(17, 248)
finger1_back_path.lineTo(13, 254)
finger1_back_path.lineTo(30, 267)
finger1_back_path.cubicTo(48, 249, 69, 227, 72, 275)
finger1_back = QGraphicsPathItem(finger1_back_path)
finger1_back.setPen(pen)
finger1_backitem = scene_girl_back.addItem(finger1_back)

hand_back_path = QPainterPath()
hand_back_path.moveTo(70, 275)
hand_back_path.cubicTo(74, 224, 0, 267, 47, 287)
hand_back = QGraphicsPathItem(hand_back_path)
hand_back.setPen(pen)
hand_backitem = scene_girl_back.addItem(hand_back)

wrist1_back_path = QPainterPath()
wrist1_back_path.moveTo(77, 282)
wrist1_back_path.cubicTo(63, 292, 59, 294, 48, 293)
wrist1_back_path.lineTo(47, 287)
wrist1_back_path.cubicTo(57, 282, 60, 286, 73, 272)
wrist1_back = QGraphicsPathItem(wrist1_back_path)
wrist1_back.setPen(pen)
wrist1_backitem = scene_girl_back.addItem(wrist1_back)

forearm1_back_path = QPainterPath()
forearm1_back_path.moveTo(60, 333)
forearm1_back_path.cubicTo(50, 327, 51, 314, 48, 294)
forearm1_back_path.cubicTo(58, 296, 61, 293, 75, 281)
forearm1_back_path.lineTo(86, 297)
forearm1_back = QGraphicsPathItem(forearm1_back_path)
forearm1_back.setPen(pen)
forearm1_backitem = scene_girl_back.addItem(forearm1_back)

elbow1_back_path = QPainterPath()
elbow1_back_path.moveTo(85, 303)
elbow1_back_path.lineTo(88, 337)
elbow1_back_path.cubicTo(71, 348, 69, 343, 61, 336)
elbow1_back = QGraphicsPathItem(elbow1_back_path)
elbow1_back.setPen(pen)
elbow1_backitem = scene_girl_back.addItem(elbow1_back)

arm1_back_path = QPainterPath()
arm1_back_path.moveTo(109, 258)
arm1_back_path.cubicTo(130, 282, 128, 277, 127, 307)
arm1_back_path.lineTo(90, 336)
arm1_back_path.lineTo(87, 297)
arm1_back = QGraphicsPathItem(arm1_back_path)
arm1_back.setPen(pen)
arm1_backitem = scene_girl_back.addItem(arm1_back)

shoulder1_back_path = QPainterPath()
shoulder1_back_path.moveTo(127, 276)
shoulder1_back_path.lineTo(133, 232)
shoulder1_back_path.cubicTo(127, 236, 122, 236, 109, 257)
shoulder1_back = QGraphicsPathItem(shoulder1_back_path)
shoulder1_back.setPen(pen)
shoulder1_backitem = scene_girl_back.addItem(shoulder1_back)

shoulder2_back_path = QPainterPath()
shoulder2_back_path.moveTo(220, 260)
shoulder2_back_path.lineTo(210, 214)
shoulder2_back_path.cubicTo(230, 222, 230, 213, 245, 234)
shoulder2_back = QGraphicsPathItem(shoulder2_back_path)
shoulder2_back.setPen(pen)
shoulder2_backitem = scene_girl_back.addItem(shoulder2_back)

arm2_back_path = QPainterPath()
arm2_back_path.moveTo(245, 236)
arm2_back_path.lineTo(274, 297)
arm2_back_path.lineTo(255, 331)
arm2_back_path.lineTo(227, 289)
arm2_back = QGraphicsPathItem(arm2_back_path)
arm2_back.setPen(pen)
arm2_backitem = scene_girl_back.addItem(arm2_back)

elbow2_back_path = QPainterPath()
elbow2_back_path.moveTo(274, 299)
elbow2_back_path.lineTo(254, 333)
elbow2_back_path.lineTo(284, 325)
elbow2_back = QGraphicsPathItem(elbow2_back_path)
elbow2_back.setPen(pen)
elbow2_backitem = scene_girl_back.addItem(elbow2_back)

forearm2_back_path = QPainterPath()
forearm2_back_path.moveTo(286, 327)
forearm2_back_path.lineTo(294, 383)
forearm2_back_path.cubicTo(281, 380, 285, 380, 270, 388)
forearm2_back_path.lineTo(259, 356)
forearm2_back_path.lineTo(256, 335)
forearm2_back = QGraphicsPathItem(forearm2_back_path)
forearm2_back.setPen(pen)
forearm2_backitem = scene_girl_back.addItem(forearm2_back)

wrist2_back_path = QPainterPath()
wrist2_back_path.moveTo(294, 385)
wrist2_back_path.cubicTo(281, 382, 284, 382, 270, 388)
wrist2_back_path.lineTo(273, 396)
wrist2_back_path.cubicTo(284, 394, 284, 392, 296, 400)
wrist2_back = QGraphicsPathItem(wrist2_back_path)
wrist2_back.setPen(pen)
wrist2_backitem = scene_girl_back.addItem(wrist2_back)

palm_back_path = QPainterPath()
palm_back_path.moveTo(285, 423)
palm_back_path.cubicTo(275, 410, 275, 405, 276, 398)
palm_back_path.cubicTo(284, 396, 284, 394, 296, 402)
palm_back_path.lineTo(300, 416)
palm_back = QGraphicsPathItem(palm_back_path)
palm_back.setPen(pen)
palm_backitem = scene_girl_back.addItem(palm_back)

finger2_back_path = QPainterPath()
finger2_back_path.moveTo(300, 418)
finger2_back_path.lineTo(301, 430)
finger2_back_path.lineTo(292, 449)
finger2_back_path.lineTo(280, 449)
finger2_back_path.lineTo(280, 443)
finger2_back_path.lineTo(287, 431)
finger2_back_path.lineTo(283, 421)
finger2_back_path.lineTo(270, 437)
finger2_back_path.lineTo(265, 431)
finger2_back_path.lineTo(271, 420)
finger2_back_path.lineTo(274, 400)
finger2_back_path.cubicTo(273, 405, 273, 410, 283, 423)
finger2_back = QGraphicsPathItem(finger2_back_path)
finger2_back.setPen(pen)
finger2_backitem = scene_girl_back.addItem(finger2_back)

back_path = QPainterPath()
back_path.moveTo(128, 308)
back_path.cubicTo(133, 347, 140, 360, 135, 386)
back_path.cubicTo(173, 381, 205, 380, 250, 391)
back_path.lineTo(245, 318)
back_path.lineTo(225, 289)
back_path.lineTo(209, 216)
back_path.lineTo(157, 218)
back_path.lineTo(135, 232)
back = QGraphicsPathItem(back_path)
back.setPen(pen)
backitem = scene_girl_back.addItem(back)

buttock_path = QPainterPath()
buttock_path.moveTo(135, 388)
buttock_path.cubicTo(173, 383, 205, 383, 250, 393)
buttock_path.cubicTo(250, 440, 225, 450, 185, 438)
buttock_path.cubicTo(145, 450, 125, 415, 135, 388)
buttock = QGraphicsPathItem(buttock_path)
buttock.setPen(pen)
buttockitem = scene_girl_back.addItem(buttock)

thigh1_back_path = QPainterPath()
thigh1_back_path.moveTo(250, 432)
thigh1_back_path.cubicTo(257, 460, 260, 470, 255, 507)
thigh1_back_path.lineTo(255, 522)
thigh1_back_path.lineTo(215, 522)
thigh1_back_path.lineTo(213, 507)
thigh1_back_path.lineTo(185, 440)
thigh1_back_path.cubicTo(225, 452, 255, 434, 252, 408)
thigh1_back = QGraphicsPathItem(thigh1_back_path)
thigh1_back.setPen(pen)
thigh1_backitem = scene_girl_back.addItem(thigh1_back)

calf1_back_path = QPainterPath()
calf1_back_path.moveTo(255, 526)
calf1_back_path.lineTo(265, 620)
calf1_back_path.lineTo(233, 620)
calf1_back_path.cubicTo(215, 585, 207, 568, 215, 526)
calf1_back = QGraphicsPathItem(calf1_back_path)
calf1_back.setPen(pen)
calf1_backitem = scene_girl_back.addItem(calf1_back)

ankle1_back = QGraphicsEllipseItem()
ankle1_back.setRect(242,621,12,12)
ankle1_back.setPen(pen)
ankle1_backitem = scene_girl_back.addItem(ankle1_back)

heel1_back_path = QPainterPath()
heel1_back_path.moveTo(239, 633)
heel1_back_path.cubicTo(225, 648, 237, 664, 259, 656)
heel1_back = QGraphicsPathItem(heel1_back_path)
heel1_back.setPen(pen)
heel1_backitem = scene_girl_back.addItem(heel1_back)

foot_back_path = QPainterPath()
foot_back_path.moveTo(261, 656)
foot_back_path.lineTo(281, 661)
foot_back_path.lineTo(291, 658)
foot_back_path.lineTo(291, 649)
foot_back_path.lineTo(273, 634)
foot_back_path.lineTo(240, 635)
foot_back = QGraphicsPathItem(foot_back_path)
foot_back.setPen(pen)
foot_backitem = scene_girl_back.addItem(foot_back)

toe_back_path = QPainterPath()
toe_back_path.moveTo(293, 658)
toe_back_path.cubicTo(317, 664, 305, 640, 288, 646)
toe_back_path.lineTo(293, 649)
toe_back = QGraphicsPathItem(toe_back_path)
toe_back.setPen(pen)
toe_backitem = scene_girl_back.addItem(toe_back)

thigh2_back_path = QPainterPath()
thigh2_back_path.moveTo(130, 426)
thigh2_back_path.lineTo(126, 520)
thigh2_back_path.lineTo(160, 537)
thigh2_back_path.lineTo(187, 455)
thigh2_back_path.lineTo(183, 440)
thigh2_back_path.cubicTo(150, 448, 157, 440, 130, 426)
thigh2_back = QGraphicsPathItem(thigh2_back_path)
thigh2_back.setPen(pen)
thigh2_backitem = scene_girl_back.addItem(thigh2_back)

calf2_back_path = QPainterPath()
calf2_back_path.moveTo(160, 539)
calf2_back_path.lineTo(125, 522)
calf2_back_path.cubicTo(115, 545, 113, 577, 116, 619)
calf2_back_path.lineTo(139, 637)
calf2_back_path.cubicTo(170, 585, 152, 549, 160, 541)
calf2_back = QGraphicsPathItem(calf2_back_path)
calf2_back.setPen(pen)
calf2_backitem = scene_girl_back.addItem(calf2_back)

ankle2_back = QGraphicsEllipseItem()
ankle2_back.setRect(113,622,12,15)
ankle2_back.setPen(pen)
ankle2_backitem = scene_girl_back.addItem(ankle2_back)

heel2_back_path = QPainterPath()
heel2_back_path.moveTo(113, 638)
heel2_back_path.lineTo(103, 657)
heel2_back_path.lineTo(108, 666)
heel2_back_path.lineTo(139, 664)
heel2_back_path.lineTo(144, 652)
heel2_back_path.lineTo(139, 639)
heel2_back = QGraphicsPathItem(heel2_back_path)
heel2_back.setPen(pen)
heel2_backitem = scene_girl_back.addItem(heel2_back)

##### SCENE WITH ALL SIX PICTURES AT A TIME #####

scene_all = QGraphicsScene(0 ,0, 450, 750)

boy_front_small = boy_front_picture.copy().scaledToHeight(310,mode=Qt.SmoothTransformation)
boy_front_small_item = scene_all.addPixmap(boy_front_small)
girl_front_small = girl_front_picture.copy().scaledToHeight(310,mode=Qt.SmoothTransformation)
girl_front_small_item = scene_all.addPixmap(girl_front_small)
girl_front_small_item.moveBy(200, 0)

boy_back_small = boy_back_picture.copy().scaledToHeight(310,mode=Qt.SmoothTransformation)
boy_back_small_item = scene_all.addPixmap(boy_back_small)
boy_back_small_item.moveBy(0, 312)
girl_back_small = girl_back_picture.copy().scaledToHeight(310,mode=Qt.SmoothTransformation)
girl_back_small_item = scene_all.addPixmap(girl_back_small)
girl_back_small_item.moveBy(200, 312)

boy_head_small = boy_head_picture.copy().scaledToWidth(200,mode=Qt.SmoothTransformation)
boy_head_small_item = scene_all.addPixmap(boy_head_small)
boy_head_small_item.moveBy(0, 624)
girl_head_small = girl_head_picture.copy().scaledToWidth(200,mode=Qt.SmoothTransformation)
girl_head_small_item = scene_all.addPixmap(girl_head_small)
girl_head_small_item.moveBy(200, 624)

boy_front = QGraphicsRectItem(0, 0, 200, 310)
pen = QPen()
pen.setStyle(Qt.NoPen)
boy_front.setPen(pen)
boy_front_item = scene_all.addItem(boy_front)

girl_front = QGraphicsRectItem(200, 0, 200, 310)
pen = QPen()
pen.setStyle(Qt.NoPen)
girl_front.setPen(pen)
girl_front_item = scene_all.addItem(girl_front)

boy_back = QGraphicsRectItem(0, 312, 200, 310)
pen = QPen()
pen.setStyle(Qt.NoPen)
boy_back.setPen(pen)
boy_back_item = scene_all.addItem(boy_back)

girl_back = QGraphicsRectItem(200, 312, 200, 310)
pen = QPen()
pen.setStyle(Qt.NoPen)
girl_back.setPen(pen)
girl_back_item = scene_all.addItem(girl_back)

boy_head = QGraphicsRectItem(0, 624, 200, 128)
pen = QPen()
pen.setStyle(Qt.NoPen)
boy_head.setPen(pen)
boy_head_item = scene_all.addItem(boy_head)

girl_head = QGraphicsRectItem(200, 624, 200, 128)
pen = QPen()
pen.setStyle(Qt.NoPen)
girl_head.setPen(pen)
girl_head_item = scene_all.addItem(girl_head)


view = MyGraphicsView(scene_all)
view.show()

##### SOUNDS #####

pygame.init()
pygame.mixer.init()

shoulder_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/bark.wav")
hip_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/biodro.wav")
eyebrow_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/brew.wav")
chin_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/broda.wav")
belly_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/brzuch.wav")
forehead_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/czolo.wav")
cleavage_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/dekolt.wav")
palm_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/dlon.wav")
head_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/glowa.wav")
tongue_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/jezyk.wav")
nape_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/kark.wav")
chest_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/klatka_piersiowa.wav")
knee_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/kolano.wav")
ankle_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/kostka.wav")
elbow_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/lokiec.wav")
calf_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/lydka.wav")
scrotum_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/moszna.wav")
wrist_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/nadgarstek.wav")
nose_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/nos.wav")
eye_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/oko.wav")
groin_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/pachwina.wav")
finger_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/palec.wav")
penis_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/penis.wav")
belly_button_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/pepek.wav")
heel_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/pieta.wav")
back_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/plecy.wav")
cheek_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/policzek.wav")
buttock_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/posladek.wav")
eyelid_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/powieka.wav")
forearm_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/przedramie.wav")
arm_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/ramie.wav")
hand_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/reka.wav")
lashes_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/rzesy.wav")
temple_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/skron.wav")
vulva_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/srom.wav")
foot_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/stopa.wav")
neck_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/szyja.wav")
torso_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/tulow.wav")
ear_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/ucho.wav")
thigh_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/udo.wav")
lips_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/usta.wav")
hair_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/wlosy.wav")
teeth_sound = pygame.mixer.Sound("/users/Programista/nauka/projekty/anatomia_dla_dzieci/dzwieki/zeby.wav")

app.exec_()
