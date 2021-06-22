
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
import pygame
import random
 
"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""
 
pygame.font.init()
 
# GLOBALS VARS
s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per blo ck
block_size = 20
 
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height - 50
 
 
# SHAPE FORMATS
 
shape = [ # redesigned
[["..0..",
      "..0..",
      "..0..",
      "..0..",
      "..0..",
      "..0..",
      "..0..",
      "..0..",
      "..0..",
      "00000",
      "00000",
      "00000"],
     
     [".....",
      "..00.",
      "..00.",
      "..00.",
      "....."]],
 
[     [".....",
      ".....",
      ".00..",
      "..0..",
      "....."],
 
     [".....",
     ".....",
      "..0..",
      ".00..",
      "....."],
 
      [".....",
      ".....",
      ".0...",
      ".00..",
      "....."],
 
      [".....",
      ".....",
      ".00..",
      ".0...",
      "....."]],
 
      [[".....",
      ".....",
      "..00.",
      "..0..",
      "....."],
 
     [".....",
     ".....",
      "..00.",
      "...0.",
      "....."],
 
      [".....",
      ".....",
      "...0.",
      "..00.",
      "....."],
 
      [".....",
      ".....",
      "..0..",
      "..00.",
      "....."],
 
      ],
 
 [	 ["..0..",
      "..0..",
      "..0..",
      "..0..",
      "....."],
     [".....",
      "0000.",
      ".....",
      ".....",
      "....."]],
 
 [	 [".....",
      "..0..",
      "..0..",
      "..0..",
      "....."],
     [".....",
      ".000.",
      ".....",
      ".....",
      "....."]],
 
[	 [".....",      
      ".00..",
      ".00..",
      "....."]],
 
[	 [".....",      
      ".....",
      "..00.",
      ".....",
      "....."],
      [".....",      
      "...0.",
      "...0.",
      ".....",
      "....."],
      ],
[[".....",
      ".0...",
      ".000.",
      ".....",
      "....."],
     [".....",
      "..00.",
      "..0..",
      "..0..",
      "....."],
     [".....",
      ".....",
      ".000.",
      "...0.",
      "....."],
     [".....",
      "..0..",
      "..0..",
      ".00..",
      "....."]],
 
[[".....",
      "...0.",
      ".000.",
      ".....",
      "....."],
     [".....",
      "..0..",
      "..0..",
      "..00.",
      "....."],
     [".....",
      ".....",
      ".000.",
      ".0...",
      "....."],
     [".....",
      ".00..",
      "..0..",
      "..0..",
      "....."]],
 
[[".....",
      "..0..",
      ".000.",
      "..0..",
      "....."]],
 
[[".....",
      "..0..",
      ".000.",
      ".....",
      "....."],
     [".....",
      "..0..",
      "..00.",
      "..0..",
      "....."],
     [".....",
      ".....",
      ".000.",
      "..0..",
      "....."],
     [".....",
      "..0..",
      ".00..",
      "..0..",
      "....."]]
     ]
 
shapes = [x for x in shape]
 
class Piece(object):
    rows = 20
    columns = 10
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = (129,200,128)
        self.rotation = 0  # number from 0-3
 
 
def create_grid(locked_positions={}):
    grid = [[(0,0,0) for x in range(10)] for x in range(20)]
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j,i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c
    return grid
 
 
def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions
 
 
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
 
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
 
    return True
 
 
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
 
 
def get_shape():
    global shapes, shape_colors
 
    return Piece(5, 0, random.choice(shapes))
 
 
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)
 
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), top_left_y + play_height/2 - label.get_height()/2))
 
 
def draw_grid(surface, row, col):
    sx = top_left_x
    sy = top_left_y
    for i in range(row):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(col):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines
 
 
def clear_rows(grid, locked):
    # need to see if row is clear the shift every other row above down one
 
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try: 
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
 
 
def draw_next_shape(shape, surface):
    font = pygame.font.SysFont("comicsans", 30)
    label = font.render("Next Shape", 1, (128,128,128))
 
    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)
 
    surface.blit(label, (sx + 10, sy- 30))
 
 
def draw_window(surface):
    surface.fill((0,0,32))
    # Tetris Title
    #font = pygame.font.SysFont("comicsans", 48)
    #label = font.render("TETRIS", 1, (255,255,255))
 
    #surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j* 30, top_left_y + i * 30, 30, 30), 0)
 
    # draw grid and border
    draw_grid(surface, 27, 10)
    pygame.draw.rect(surface, (128, 128, 128), (top_left_x, top_left_y, play_width, play_height), 5)
    #pygame.display.update()
 
 
def main():
    global grid
 
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
 
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
 
    while run:
        fall_speed = 0.27
 
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
 
        # PIECE FALLING CODE
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
 
            if event.type == pygame.KEYDOWN:
 
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
 
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_UP:
                    # rotate shape
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
 
                if event.key == pygame.K_SPACE:
                   while valid_space(current_piece, grid):
                       current_piece.y += 1
                   current_piece.y -= 1
                   #print(convert_shape_format(current_piece))"""  # todo fix
 
 
        shape_pos = convert_shape_format(current_piece)
 
        # add piece to the grid for drawing
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
 
        # IF PIECE HIT GROUND
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
 
            # call four times to check for multiple clear rows
            clear_rows(grid, locked_positions)
 
        draw_window(win)
        draw_next_shape(next_piece, win)
        pygame.display.update()
 
        # Check if user lost
        if check_lost(locked_positions):
            run = False
 
    draw_text_middle("You Lost", 40, (255,255,255), win)
    pygame.display.update()
    pygame.time.delay(2000)
 
 
def main_menu():
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle("Press any key to begin.", 60, (255, 255, 255), win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
 
            if event.type == pygame.KEYDOWN:
                main()
    pygame.quit()
 
 
win = pygame.display.set_mode((s_width, s_height))
#win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Tetris")
main_menu()  # start game