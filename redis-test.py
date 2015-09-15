# -*- coding: utf-8 -*-

"""
Created on Sun Sep 13 19:55:32 2015

@author: rob

"""

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.flushdb

r.set('K1', 'V1')
                                        
print 'The Key that was SET : ' + r.get('K1')

r.set('C', 1)
r.incr('C')

print 'The Counter was INCR to : '+ r.get('C')

r.decr('C')

print 'The Counter was DECR to : '+ r.get('C')

r.rpush('L1', 'E1')

r.rpush('L1', 'E2')
r.rpush('L2', 'E3')

print 'The List length is : %s' % r.llen('L1')

print 'The Element at position 0 of the List is : %s' % r.lindex('L1', 0)

print 'The Element at position 1 of the List is : %s' % r.lindex('L1', 1)

print 'The Element at position 5 of the List is : %s' % r.lindex('L1', 5)

r.sadd('S1', 'E1')
r.sadd('S1', 'E2')
r.sadd('S1', 'E2')

print 'The Members of our Set are : %s' % r.smembers('S1')
