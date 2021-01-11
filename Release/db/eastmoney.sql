/*
Navicat MySQL Data Transfer

Source Server         : 10.1.27.237_3306
Source Server Version : 80016
Source Host           : 10.1.27.237:3306
Source Database       : eastmoney

Target Server Type    : MYSQL
Target Server Version : 80016
File Encoding         : 65001

Date: 2021-01-11 16:07:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for bk
-- ----------------------------
DROP TABLE IF EXISTS `bk`;
CREATE TABLE `bk` (
  `日期` datetime NOT NULL,
  `板块代码` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `板块名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `最新值` float DEFAULT NULL,
  `涨幅` float DEFAULT NULL,
  `主力净流入` float DEFAULT NULL,
  `主力净流入占比` float DEFAULT NULL,
  `超大单净流入` float DEFAULT NULL,
  `超大单净流入占比` float DEFAULT NULL,
  `大单净流入` float DEFAULT NULL,
  `大单净流入占比` float DEFAULT NULL,
  `中单净流入` float DEFAULT NULL,
  `中单净流入占比` float DEFAULT NULL,
  `小单净流入` float DEFAULT NULL,
  `小单净流入占比` float DEFAULT NULL,
  `龙头` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`日期`,`板块代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bkday
-- ----------------------------
DROP TABLE IF EXISTS `bkday`;
CREATE TABLE `bkday` (
  `日期` date NOT NULL,
  `板块代码` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `板块名` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `最新值` float DEFAULT NULL,
  `涨幅` float DEFAULT NULL,
  `总成交` float DEFAULT NULL,
  `主力净流入` float DEFAULT NULL,
  `主力净流入占比` float DEFAULT NULL,
  `超大单净流入` float DEFAULT NULL,
  `超大单净流入占比` float DEFAULT NULL,
  `大单净流入` float DEFAULT NULL,
  `大单净流入占比` float DEFAULT NULL,
  `中单净流入` float DEFAULT NULL,
  `中单净流入占比` float DEFAULT NULL,
  `小单净流入` float DEFAULT NULL,
  `小单净流入占比` float DEFAULT NULL,
  `龙头` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`日期`,`板块代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for bkgp
-- ----------------------------
DROP TABLE IF EXISTS `bkgp`;
CREATE TABLE `bkgp` (
  `板块代码` varchar(20) DEFAULT NULL,
  `证券代码` varchar(20) DEFAULT NULL,
  `公司名` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for companyinfo
-- ----------------------------
DROP TABLE IF EXISTS `companyinfo`;
CREATE TABLE `companyinfo` (
  `证券代码` varchar(20) NOT NULL,
  `公司名` varchar(20) DEFAULT NULL,
  `总股本` bigint(20) DEFAULT NULL,
  `流通股本` bigint(20) DEFAULT NULL,
  `上市日期` date DEFAULT NULL,
  `公司简介` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `所属板块` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `主营业务` varchar(1024) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `主营产品` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  `上市状态` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`证券代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for convertiblebond
-- ----------------------------
DROP TABLE IF EXISTS `convertiblebond`;
CREATE TABLE `convertiblebond` (
  `转债代码` varchar(20) NOT NULL,
  `转债名称` varchar(20) NOT NULL,
  `转债最新价` float(10,3) DEFAULT NULL,
  `转债涨跌幅` float(10,3) DEFAULT NULL,
  `正股代码` varchar(20) DEFAULT NULL,
  `正股名称` varchar(20) DEFAULT NULL,
  `最新价` float(10,3) DEFAULT NULL,
  `涨跌幅` float(10,3) DEFAULT NULL,
  `转股价` float(10,3) DEFAULT NULL,
  `转股价值` float(10,3) DEFAULT NULL,
  `转股溢价率` float(10,3) DEFAULT NULL,
  `纯债溢价率` float(10,3) DEFAULT NULL,
  `回售触发价` float(10,3) DEFAULT NULL,
  `强赎触发价` float(10,3) DEFAULT NULL,
  `到期赎回价` float(10,3) DEFAULT NULL,
  `纯债价值` float(10,3) DEFAULT NULL,
  `开始转股日` date DEFAULT NULL,
  `上市日期` date DEFAULT NULL,
  `申购日期` date DEFAULT NULL,
  PRIMARY KEY (`转债代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for day
-- ----------------------------
DROP TABLE IF EXISTS `day`;
CREATE TABLE `day` (
  `日期` date NOT NULL,
  `证券代码` varchar(20) NOT NULL,
  `公司名` varchar(20) DEFAULT NULL,
  `涨幅` float DEFAULT NULL,
  `开盘价` float DEFAULT NULL,
  `昨收价` float DEFAULT NULL,
  `当前价` float DEFAULT NULL,
  `最高价` float DEFAULT NULL,
  `最低价` float DEFAULT NULL,
  `成交量` float DEFAULT NULL,
  `成交额` float DEFAULT NULL,
  `换手率` float DEFAULT NULL,
  PRIMARY KEY (`日期`,`证券代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for lhb
-- ----------------------------
DROP TABLE IF EXISTS `lhb`;
CREATE TABLE `lhb` (
  `日期` date NOT NULL,
  `证券代码` varchar(20) NOT NULL,
  `公司名` varchar(20) DEFAULT NULL,
  `收盘价` float DEFAULT NULL,
  `涨幅` float DEFAULT NULL,
  `换手` float DEFAULT NULL,
  `净买额` float DEFAULT NULL,
  `总金额` float DEFAULT NULL,
  `总成交手` float DEFAULT NULL,
  `上榜类型` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `总卖` float DEFAULT NULL,
  `总买` float DEFAULT NULL,
  `净买占总成交比` float DEFAULT NULL,
  `流通市值` float DEFAULT NULL,
  `解读` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`日期`,`证券代码`,`上榜类型`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sinareal
-- ----------------------------
DROP TABLE IF EXISTS `sinareal`;
CREATE TABLE `sinareal` (
  `日期` datetime NOT NULL,
  `证券代码` varchar(20) NOT NULL,
  `公司名` varchar(20) DEFAULT NULL,
  `涨幅` float DEFAULT NULL,
  `开盘价` float DEFAULT NULL,
  `昨收价` float DEFAULT NULL,
  `当前价` float DEFAULT NULL,
  `最高价` float DEFAULT NULL,
  `最低价` float DEFAULT NULL,
  `竞买价` float DEFAULT NULL,
  `竞卖价` float DEFAULT NULL,
  `成交量` float DEFAULT NULL,
  `成交额` float DEFAULT NULL,
  `买一量` float DEFAULT NULL,
  `买一价` float DEFAULT NULL,
  `买二量` float DEFAULT NULL,
  `买二价` float DEFAULT NULL,
  `买三量` float DEFAULT NULL,
  `买三价` float DEFAULT NULL,
  `买四量` float DEFAULT NULL,
  `买四价` float DEFAULT NULL,
  `买五量` float DEFAULT NULL,
  `买五价` float DEFAULT NULL,
  `卖一量` float DEFAULT NULL,
  `卖一价` float DEFAULT NULL,
  `卖二量` float DEFAULT NULL,
  `卖二价` float DEFAULT NULL,
  `卖三量` float DEFAULT NULL,
  `卖三价` float DEFAULT NULL,
  `卖四量` float DEFAULT NULL,
  `卖四价` float DEFAULT NULL,
  `卖五量` float DEFAULT NULL,
  `卖五价` float DEFAULT NULL,
  PRIMARY KEY (`日期`,`证券代码`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
