# dslab_mongo
Svetlana Kabirova 
SE-01

Screen 1: https://ibb.co/3Cr463D

![Screenshot](ph1.jpg)

rs.config()
```json 
{
        "_id" : "rs0",
        "version" : 66285,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "f.inst.lan:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 0.5,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "s.inst.lan:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 0.5,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "172.31.82.137:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbc883d92a40c3857c3fad3")
        }
}
```

rs.status():
```json 
{
        "set" : "rs0",
        "date" : ISODate("2019-11-01T22:10:50.910Z"),
        "myState" : 1,
        "term" : NumberLong(2),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572646241, 1),
                        "t" : NumberLong(2)
                },
                "lastCommittedWallTime" : ISODate("2019-11-01T22:10:41.020Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572646241, 1),
                        "t" : NumberLong(2)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-01T22:10:41.020Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572646241, 1),
                        "t" : NumberLong(2)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572646241, 1),
                        "t" : NumberLong(2)
                },
                "lastAppliedWallTime" : ISODate("2019-11-01T22:10:41.020Z"),
                "lastDurableWallTime" : ISODate("2019-11-01T22:10:41.020Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572646221, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572646221, 1),
        "electionCandidateMetrics" : {
                "lastElectionReason" : "electionTimeout",
                "lastElectionDate" : ISODate("2019-11-01T20:32:30.249Z"),
                "termAtElection" : NumberLong(2),
                "lastCommittedOpTimeAtElection" : {
                        "ts" : Timestamp(0, 0),
                        "t" : NumberLong(-1)
                },
                "lastSeenOpTimeAtElection" : {
                        "ts" : Timestamp(1572640281, 1),
                        "t" : NumberLong(1)
                },
                "numVotesNeeded" : 2,
                "priorityAtElection" : 1,
                "electionTimeoutMillis" : NumberLong(10000),
                "numCatchUpOps" : NumberLong(808464432),
                "newTermStartDate" : ISODate("2019-11-01T20:32:30.861Z"),
                "wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T20:32:32.322Z")
        },
        "members" : [
                {
                        "_id" : 0,
                        "name" : "f.inst.lan:27017",
                        "ip" : "172.31.85.234",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 5896,
                        "optime" : {
                                "ts" : Timestamp(1572646241, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572646241, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-01T22:10:41Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T22:10:41Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T22:10:49.638Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T22:10:50.324Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "172.31.82.137:27017",
                        "syncSourceHost" : "172.31.82.137:27017",
                        "syncSourceId" : 2,
                        "infoMessage" : "",
                        "configVersion" : 66285
                },
                {
                        "_id" : 1,
                        "name" : "s.inst.lan:27017",
                        "ip" : "172.31.92.129",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 5903,
                        "optime" : {
                                "ts" : Timestamp(1572646241, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572646241, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-01T22:10:41Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T22:10:41Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T22:10:49.250Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T22:10:49.766Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "172.31.82.137:27017",
                        "syncSourceHost" : "172.31.82.137:27017",
                        "syncSourceId" : 2,
                        "infoMessage" : "",
                        "configVersion" : 66285
                },
                {
                        "_id" : 2,
                        "name" : "172.31.82.137:27017",
                        "ip" : "172.31.82.137",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 5912,
                        "optime" : {
                                "ts" : Timestamp(1572646241, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-01T22:10:41Z"),
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572640350, 1),
                        "electionDate" : ISODate("2019-11-01T20:32:30Z"),
                        "configVersion" : 66285,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572646241, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572646241, 1)
}
```
### Minus 1 VPS

Screen 2: https://ibb.co/ssnWHNP

![Screenshot](ph2.jpg)

rs.config():
```json 
{
        "_id" : "rs0",
        "version" : 66285,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "f.inst.lan:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 0.5,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "s.inst.lan:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 0.5,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "172.31.82.137:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbc883d92a40c3857c3fad3")
        }
}
```

rs.status():
```json 
{
        "set" : "rs0",
        "date" : ISODate("2019-11-01T22:21:21.952Z"),
        "myState" : 2,
        "term" : NumberLong(3),
        "syncingTo" : "s.inst.lan:27017",
        "syncSourceHost" : "s.inst.lan:27017",
        "syncSourceId" : 1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572646880, 1),
                        "t" : NumberLong(3)
                },
                "lastCommittedWallTime" : ISODate("2019-11-01T22:21:20.037Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572646880, 1),
                        "t" : NumberLong(3)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-01T22:21:20.037Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572646880, 1),
                        "t" : NumberLong(3)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572646880, 1),
                        "t" : NumberLong(3)
                },
                "lastAppliedWallTime" : ISODate("2019-11-01T22:21:20.037Z"),
                "lastDurableWallTime" : ISODate("2019-11-01T22:21:20.037Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572646830, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572646830, 1),
        "members" : [
                {
                        "_id" : 0,
                        "name" : "f.inst.lan:27017",
                        "ip" : "172.31.85.234",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 6529,
                        "optime" : {
                                "ts" : Timestamp(1572646880, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDate" : ISODate("2019-11-01T22:21:20Z"),
                        "syncingTo" : "s.inst.lan:27017",
                        "syncSourceHost" : "s.inst.lan:27017",
                        "syncSourceId" : 1,
                        "infoMessage" : "",
                        "configVersion" : 66285,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "s.inst.lan:27017",
                        "ip" : "172.31.92.129",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 6528,
                        "optime" : {
                                "ts" : Timestamp(1572646880, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572646880, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDate" : ISODate("2019-11-01T22:21:20Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T22:21:20Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T22:21:20.972Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T22:21:21.544Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572646369, 1),
                        "electionDate" : ISODate("2019-11-01T22:12:49Z"),
                        "configVersion" : 66285
                },
                {
                        "_id" : 2,
                        "name" : "172.31.82.137:27017",
                        "ip" : "172.31.82.137",
                        "health" : 0,
                        "state" : 8,
                        "stateStr" : "(not reachable/healthy)",
                        "uptime" : 0,
                        "optime" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
                        "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T22:21:18.696Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T22:12:49.660Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "Error connecting to 172.31.82.137:27017 :: caused by :: No route to host",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "configVersion" : -1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572646880, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572646880, 1)
}
```


