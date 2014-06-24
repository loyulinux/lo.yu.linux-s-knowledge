-- 2014年 6月22日 星期日 18时37分29秒 CST
CREATE TABLE T_INSTANCE(
    ID BIGINT(10) AUTO_INCREMENT PRIMARY KEY COMMENT 'MySQL实例表主键ID',
    NAME VARCHAR(30)  CHAR SET UTF8 COLLATE UTF8_GENERAL_CI NOT NULL COMMENT 'MySQL实例名',
    IP INT DEFAULT 0 COMMENT 'MySQL实例的IP地址',
    PORT INT DEFAULT 3306 COMMENT 'MySQL实例监听端口',
    STATE INT DEFAULT 0 COMMENT 'MySQL实例状态:0停止;1运行;2临时下线',
    USER VARCHAR(20) CHAR SET UTF8 NOT NULL COMMENT 'MySQL实例用户名',
    PASSWD VARCHAR(20) CHAR SET UTF8 NOT NULL DEFAULT '' COMMENT '加密后的MySQL用户密码'
) ENGINE=MyISAM;

CREATE TABLE T_ALERT(
    ID BIGINT(10) AUTO_INCREMENT PRIMARY KEY COMMENT '告警通知表主键ID',
    INSTANCE BIGINT(10) NOT NULL COMMENT '告警实例ID',
    EVENT_NAME VARCHAR(40) CHAR SET UTF8 COLLATE UTF8_GENERAL_CI COMMENT '告警原因',
    EVENT_BODY VARCHAR(500) CHAR SET UTF8 COLLATE UTF8_GENERAL_CI COMMENT '告警通知正文',
    LEVEL INT DEFAULT 0 COMMENT '告警等级:0警告,1错误,2紧急',
    RECEIVER VARCHAR(20) COMMENT '接受告警邮箱',
    STATE INT COMMENT '告警发送状态'
) ENGINE=InnoDB;

CREATE TABLE T_CONNECTION(
    ID BIGINT(10) AUTO_INCREMENT PRIMARY KEY COMMENT '连接数表主键ID',
    INSTANCE BIGINT(10) COMMENT '连接所在实例',
    CNT INT COMMENT '连接数',
    CHECKTIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '检测连接数时间'
) ENGINE=InnoDB;

CREATE TABLE T_QUERY(
    ID BIGINT(10) AUTO_INCREMENT PRIMARY KEY COMMENT 'SQL查询表主键ID',
    INSTANCE BIGINT(10) COMMENT '查询所在实例',
    SQLBODY VARCHAR(200) COMMENT 'SQL',
    CHECKSUM varchar(64) COMMENT 'SQL的CHECKSUM值',
    EXECTIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'SQL执行的时间点'
) ENGINE=InnoDB;
