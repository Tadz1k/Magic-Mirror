SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `mirror_notes`
-- ----------------------------
DROP TABLE IF EXISTS `mirror_notes`;
CREATE TABLE `mirror_notes` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `note1` varchar(256) NOT NULL DEFAULT '',
  `note2` varchar(256) NOT NULL DEFAULT '',
  `note3` varchar(256) NOT NULL DEFAULT '',
  `priority1` int(3) NOT NULL DEFAULT '1',
  `priority2` int(3) NOT NULL DEFAULT '1',
  `priority3` int(3) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of mirror_notes
-- ----------------------------
INSERT INTO `mirror_notes` VALUES ('1', 'note1', 'note2', 'note3', '2', '3', '1');
