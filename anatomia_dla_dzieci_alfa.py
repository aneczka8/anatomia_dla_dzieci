from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * #QBrush, QPainter, QPen, QPixmap, QPolygonF
import sys
import pygame

app = QApplication(sys.argv)

def set_body_part_visible(a, b):
    boy_front_picture_item.setVisible(a)
    girl_front_picture_item.setVisible(b)

class MyGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.Antialiasing)
        self.zoomed_in = False
        self.active_scene = scene_all
    
    def mousePressEvent(self, event):
        ### ADD BODY PARTS SOUNDS ###
        pos = self.mapToScene(event.pos())

        eye1_pos = eye1.mapFromScene(pos)
        eye2_pos = eye2.mapFromScene(pos)   
        nose_pos = nose.mapFromScene(pos)
        eyebrow1_pos = eyebrow1.mapFromScene(pos)
        eyebrow2_pos = eyebrow2.mapFromScene(pos)
        lashes1_pos = lashes1.mapFromScene(pos)
        lashes2_pos = lashes2.mapFromScene(pos)
        tongue_pos = tongue.mapFromScene(pos)
        teeth_pos = teeth.mapFromScene(pos)
        cheek1_pos = cheek1.mapFromScene(pos)
        cheek2_pos = cheek2.mapFromScene(pos)
        ear_pos = ear.mapFromScene(pos)
        temple_pos = temple.mapFromScene(pos)
        chin_pos = chin.mapFromScene(pos)
        neck_pos = neck.mapFromScene(pos)
        cleavage_pos = cleavage.mapFromScene(pos)
        chest_pos = chest.mapFromScene(pos)
        belly_pos = belly.mapFromScene(pos)
        penis_pos = penis.mapFromScene(pos)
        scrotum_pos = scrotum.mapFromScene(pos)
        vulva_pos = vulva.mapFromScene(pos)
        shoulder1_pos = shoulder1.mapFromScene(pos)
        shoulder2_pos = shoulder2.mapFromScene(pos)
        arm1_pos = arm1.mapFromScene(pos)
        arm2_pos = arm2.mapFromScene(pos)
        elbow1_pos = elbow1.mapFromScene(pos)
        elbow2_pos = elbow2.mapFromScene(pos)
        forearm1_pos = forearm1.mapFromScene(pos)
        forearm2_pos = forearm2.mapFromScene(pos)
        wrist1_pos = wrist1.mapFromScene(pos)
        wrist2_pos = wrist2.mapFromScene(pos)
        palm_pos = palm.mapFromScene(pos)
        finger1_pos = finger1.mapFromScene(pos)
        finger2_pos = finger2.mapFromScene(pos)
        hand_pos = hand.mapFromScene(pos)
        hip1_pos = hip1.mapFromScene(pos)
        hip2_pos = hip2.mapFromScene(pos)
        thigh1_pos = thigh1.mapFromScene(pos)
        thigh2_pos = thigh2.mapFromScene(pos)
        knee1_pos = knee1.mapFromScene(pos)
        knee2_pos = knee2.mapFromScene(pos)
        calf1_pos = calf1.mapFromScene(pos)
        calf2_pos = calf2.mapFromScene(pos)
        heel_pos = heel.mapFromScene(pos)
        foot1_pos = foot1.mapFromScene(pos)
        foot2_pos = foot2.mapFromScene(pos)
        toe1_pos = toe1.mapFromScene(pos)
        toe2_pos = toe2.mapFromScene(pos)
        ankle_pos = ankle.mapFromScene(pos)
        forehead_boy_pos = forehead_boy.mapFromScene(pos)
        hair_boy_pos = hair_boy.mapFromScene(pos)
        forehead1_girl_pos = forehead1_girl.mapFromScene(pos)
        forehead2_girl_pos = forehead2_girl.mapFromScene(pos)
        hair_girl_pos = hair_girl.mapFromScene(pos)


        if self.active_scene == scene_boy_front or self.active_scene == scene_girl_front:
            if eye1.contains(eye1_pos) or eye2.contains(eye2_pos):
                eye_sound.play()

            elif nose.contains(nose_pos):
                nose_sound.play()

            elif eyebrow1.contains(eyebrow1_pos) or eyebrow2.contains(eyebrow2_pos):
                eyebrow_sound.play()

            elif lashes1.contains(lashes1_pos) or lashes2.contains(lashes2_pos):
                lashes_sound.play()

            elif tongue.contains(tongue_pos):
                tongue_sound.play()

            elif teeth.contains(teeth_pos):
                teeth_sound.play()

            elif cheek1.contains(cheek1_pos) or cheek2.contains(cheek2_pos):
                cheek_sound.play()

            elif ear.contains(ear_pos):
                ear_sound.play()

            elif temple.contains(temple_pos):
                temple_sound.play()

            elif chin.contains(chin_pos):
                chin_sound.play()
                
            elif neck.contains(neck_pos):
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

            elif forehead_boy.contains(forehead_boy_pos):
                forehead_sound.play()

            elif hair_boy.contains(hair_boy_pos):
                hair_sound.play()

        if self.active_scene == scene_girl_front:
            if vulva.contains(vulva_pos):
                vulva_sound.play()

            elif forehead1_girl.contains(forehead1_girl_pos) or forehead2_girl.contains(forehead2_girl_pos):
                forehead_sound.play()

            elif hair_girl.contains(hair_girl_pos):
                hair_sound.play()

    def mouseDoubleClickEvent(self, event):
    ### CHOOSE PICTURE ###
        pos = self.mapToScene(event.pos())

        boy_front_pos = boy_front.mapFromScene(pos)
        girl_front_pos = girl_front.mapFromScene(pos)

        if not self.zoomed_in:
            self.zoomed_in = True
            if boy_front.contains(boy_front_pos):
                set_body_part_visible(True, False)
                self.setScene(scene_boy_front)
                self.active_scene = scene_boy_front
            elif girl_front.contains(girl_front_pos):
                set_body_part_visible(False, True)
                self.setScene(scene_girl_front)
                self.active_scene = scene_girl_front

        else:
            self.setScene(scene_all)
            self.zoomed_in = False
            self.active_scene = scene_all

##### SCENE WITH ONE PICTURE AT A TIME ###### 
              
scene_boy_front = QGraphicsScene(0, 0, 450, 750)
scene_girl_front = QGraphicsScene(0, 0, 450, 750)

boy_front_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/boy_front.jpeg").scaledToHeight(700,mode=Qt.SmoothTransformation)
boy_front_picture_item = scene_boy_front.addPixmap(boy_front_picture)
girl_front_picture = QPixmap("/users/Programista/nauka/projekty/anatomia_dla_dzieci/obrazki/girl_front.jpeg").scaledToHeight(700,mode=Qt.SmoothTransformation)
girl_front_picture_item = scene_girl_front.addPixmap(girl_front_picture)

girl_front_picture_item.setVisible(False)
boy_front_picture_item.setVisible(False)

pen = QPen(Qt.green)
pen.setStyle(Qt.NoPen)

eye1_path = QPainterPath()
eye1_path.moveTo(160, 145)
eye1_path.cubicTo(170, 115, 190, 115, 200, 145)
eye1_path.cubicTo(190, 155, 170, 155, 160, 145)
eye1 = QGraphicsPathItem(eye1_path)
eye1.setPen(pen)
eye1item = scene_boy_front.addItem(eye1)

eye2_path = QPainterPath()
eye2_path.moveTo(229, 144)
eye2_path.cubicTo(225, 112, 249, 115, 255, 142)
eye2_path.cubicTo(237, 148, 235, 148, 229, 144)
eye2 = QGraphicsPathItem(eye2_path)
eye2.setPen(pen)
eyeitem2 = scene_boy_front.addItem(eye2)

nose_path = QPainterPath()
nose_path.moveTo(212, 141)
nose_path.cubicTo(215, 150, 207, 145, 223, 155)
nose_path.cubicTo(218, 163, 215, 163, 210, 160)
nose = QGraphicsPathItem(nose_path)
nose.setPen(pen)
noseitem = scene_boy_front.addItem(nose)

eyebrow1_path = QPainterPath()
eyebrow1_path.moveTo(168, 115)
eyebrow1_path.cubicTo(180, 107, 175, 106, 190, 109)
eyebrow1_path.lineTo(190, 111)
eyebrow1_path.cubicTo(170, 112, 185, 111, 168, 118)
eyebrow1_path.lineTo(168, 115)
eyebrow1 = QGraphicsPathItem(eyebrow1_path)
eyebrow1.setPen(pen)
eyebrow1item = scene_boy_front.addItem(eyebrow1)

eyebrow2_path = QPainterPath()
eyebrow2_path.moveTo(234, 108)
eyebrow2_path.cubicTo(245, 108, 240, 106, 253, 117)
eyebrow2_path.lineTo(251, 118)
eyebrow2_path.cubicTo(245, 109, 234, 110, 234, 110)
eyebrow2_path.lineTo(234, 108)
eyebrow2 = QGraphicsPathItem(eyebrow2_path)
eyebrow2.setPen(pen)
eyebrow2item = scene_boy_front.addItem(eyebrow2)

lashes1_path = QPainterPath()
lashes1_path.moveTo(155, 144)
lashes1_path.cubicTo(166, 115, 156, 130, 173, 120)
lashes1_path.lineTo(174,122)
lashes1_path.cubicTo(160, 135, 165, 125, 158, 145)
lashes1 = QGraphicsPathItem(lashes1_path)
lashes1.setPen(pen)
lashes1item = scene_boy_front.addItem(lashes1)

lashes2_path = QPainterPath()
lashes2_path.moveTo(257, 142)
lashes2_path.cubicTo(253, 130, 260, 137, 249, 125)
lashes2_path.lineTo(253,122)
lashes2_path.cubicTo(260, 130, 255, 125, 262, 140)
lashes2 = QGraphicsPathItem(lashes2_path)
lashes2.setPen(pen)
lashes2item = scene_boy_front.addItem(lashes2)

tongue_path = QPainterPath()
tongue_path.moveTo(176, 174)
tongue_path.cubicTo(195, 175, 205, 170, 214, 182)
tongue_path.cubicTo(205, 185, 197, 180, 180, 178)
tongue = QGraphicsPathItem(tongue_path)
tongue.setPen(pen)
tongueitem = scene_boy_front.addItem(tongue)

teeth_path = QPainterPath()
teeth_path.moveTo(220, 183)
teeth_path.cubicTo(205, 188, 197, 183, 180, 181)
teeth_path.cubicTo(195, 190, 208, 194, 220, 183)
teeth = QGraphicsPathItem(teeth_path)
teeth.setPen(pen)
teethitem = scene_boy_front.addItem(teeth)

cheek1 = QGraphicsEllipseItem()
cheek1.setRect(139,148,31,31)
cheek1.setPen(pen)
cheek1item = scene_boy_front.addItem(cheek1)

cheek2_path = QPainterPath()
cheek2_path.moveTo(250, 177)
cheek2_path.cubicTo(225, 180, 230, 135, 262, 155)
cheek2_path.cubicTo(260, 168, 261, 165, 250, 177)
cheek2 = QGraphicsPathItem(cheek2_path)
cheek2.setPen(pen)
cheek2item = scene_boy_front.addItem(cheek2)

ear_path = QPainterPath()
ear_path.moveTo(139, 163)
ear_path.cubicTo(110, 158, 106, 110, 134, 131)
ear = QGraphicsPathItem(ear_path)
ear.setPen(pen)
earitem = scene_boy_front.addItem(ear)

temple = QGraphicsEllipseItem()
temple.setRect(145,123,12,20)
temple.setPen(pen)
templeitem = scene_boy_front.addItem(temple)

chin_path = QPainterPath()
chin_path.moveTo(187, 203)
chin_path.lineTo(190, 195)
chin_path.lineTo(222, 195)
chin_path.lineTo(224, 200)
chin_path.cubicTo(213, 207, 205, 210, 187, 203)
chin = QGraphicsPathItem(chin_path)
chin.setPen(pen)
chinitem = scene_boy_front.addItem(chin)

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
forehead_boy_path.moveTo(272, 115)
forehead_boy_path.cubicTo(220, 100, 180, 104, 145, 114)
forehead_boy_path.lineTo(170, 91)
forehead_boy_path.lineTo(166, 106)
forehead_boy_path.lineTo(192, 95)
forehead_boy_path.lineTo(204, 78)
forehead_boy_path.lineTo(204, 93)
forehead_boy_path.cubicTo(222, 93, 234, 85, 244, 66)
forehead_boy_path.cubicTo(264, 76, 270, 104, 272, 115)
forehead_boy = QGraphicsPathItem(forehead_boy_path)
forehead_boy.setPen(pen)
forehead_boyitem = scene_boy_front.addItem(forehead_boy)

hair_boy_path = QPainterPath()
hair_boy_path.moveTo(145, 145)
hair_boy_path.cubicTo(138, 115, 150, 100, 171, 90)
hair_boy_path.lineTo(171, 90)
hair_boy_path.lineTo(166, 105)
hair_boy_path.lineTo(192, 94)
hair_boy_path.lineTo(204, 77)
hair_boy_path.lineTo(205, 91)
hair_boy_path.cubicTo(222, 91, 234, 83, 244, 64)
hair_boy_path.cubicTo(266, 76, 280, 104, 272, 143)
hair_boy_path.cubicTo(340, 105, 250, 5, 215, 8)
hair_boy_path.cubicTo(85, 0, 40, 155, 130, 170)
hair_boy_path.lineTo(130, 162)
hair_boy_path.cubicTo(109, 158, 104, 108, 134, 129)
hair_boy_path.lineTo(135, 141)
hair_boy = QGraphicsPathItem(hair_boy_path)
hair_boy.setPen(pen)
hair_boyitem = scene_boy_front.addItem(hair_boy)

forehead1_girl_path = QPainterPath()
forehead1_girl_path.moveTo(260, 112)
forehead1_girl_path.cubicTo(220, 100, 180, 104, 165, 110)
forehead1_girl_path.cubicTo(190, 88, 211, 85, 220, 63)
forehead1_girl_path.cubicTo(235, 83, 260, 94, 260, 112)
forehead1_girl = QGraphicsPathItem(forehead1_girl_path)
forehead1_girl.setPen(pen)
forehead1_girlitem = scene_girl_front.addItem(forehead1_girl)

forehead2_girl_path = QPainterPath()
forehead2_girl_path.moveTo(145, 115)
forehead2_girl_path.cubicTo(150, 105, 150, 104, 168, 90)
forehead2_girl_path.lineTo(160, 113)
forehead2_girl = QGraphicsPathItem(forehead2_girl_path)
forehead2_girl.setPen(pen)
forehead2_girlitem = scene_girl_front.addItem(forehead2_girl)

hair_girl_path = QPainterPath()
hair_girl_path.moveTo(145, 145)
hair_girl_path.cubicTo(138, 115, 150, 100, 168, 89)
hair_girl_path.lineTo(161, 112)
hair_girl_path.cubicTo(190, 86, 211, 83, 220, 61)
hair_girl_path.cubicTo(235, 82, 260, 93, 265, 122)
hair_girl_path.lineTo(270, 109)
hair_girl_path.cubicTo(275, 142, 270, 150, 257, 175)
hair_girl_path.cubicTo(258, 285, 359, 163, 268, 152) #kitka
hair_girl_path.cubicTo(350, 105, 280, 0, 205, 13)
hair_girl_path.cubicTo(85, 0, 70, 135, 97, 152)
hair_girl_path.cubicTo(0, 170, 105, 290, 110, 165) #kitka
hair_girl_path.lineTo(140, 180)
hair_girl_path.lineTo(130, 162)
hair_girl_path.cubicTo(109, 158, 104, 108, 134, 129)
hair_girl_path.lineTo(135, 141)
hair_girl = QGraphicsPathItem(hair_girl_path)
hair_girl.setPen(pen)
hair_girlitem = scene_girl_front.addItem(hair_girl)

##### SCENE WITH ALL SIX PICTURES AT A TIME #####

scene_all = QGraphicsScene(0 ,0, 450, 750)

boy_front_small = boy_front_picture.copy().scaledToHeight(310,mode=Qt.SmoothTransformation)
boy_front_small_item = scene_all.addPixmap(boy_front_small)
girl_front_small = girl_front_picture.copy().scaledToHeight(310,mode=Qt.SmoothTransformation)
girl_front_small_item = scene_all.addPixmap(girl_front_small)
girl_front_small_item.moveBy(200, 0)

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
