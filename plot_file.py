from bokeh.plotting import figure, output_file, show

output_file("line.html")

p = figure(plot_width=400, plot_height=400)

raw_data_1 = """0.18963
0.00615
0.05242
0.10016
0.16402
0.15021
0.06402
0.12767
0.02732
0.08481
0.03839
0.11687
0.0492
0.01029
0.02648
0.10733
0.16472
0.14561
0.03974
0.02077
0.11349
0.07893
0.09204
0.16546
0.19985
0.10981
0.18789
0.1972
0.10633
0.02599
0.15032
0.07725
0.08333
0.15301
0.19951
0.05266
0.02402
0.08755
0.03072
0.19332
0.16285
0.07895
0.03822
0.07857
0.11063
0.19748
0.18114
0.13284
0.07544
0.06482
0.04203
0.09654
0.0766
0.1691
0.14633
0.13365
0.1994
0.17818
0.08629
0.19697
0.04549
0.13624
0.14936
0.04455
0.05564
0.07432
0.15733
0.1116
0.18412
0.05536
0.16199
0.11493
0.08854
0.1445
0.10777
0.06766
0.086
0.02239
0.00448
0.08353
0.15261
0.04759
0.00115
0.13424
0.02071
0.10464
0.19156
0.14329
0.07869
0.00264
0.13576
0.00991
0.15437
0.09812
0.08094
0.17874
0.19533
0.03872
0.09662
0.08048
0.07364
0.01491
0.1567
0.11852
0.07792
0.12578
0.04847
0.13418
0.14793
0.11695
0.02779
0.06016
0.03228
0.07838
0.00929
0.04076
0.15228
0.10269
0.17623
0.02899
0.12055
0.18344
0.1238
0.14326
0.14414
0.186
0.08784
0.13675
0.11296
0.13353
0.01678
0.19075
0.02299
0.09881
0.0042
0.19244
0.17523
0.01435
0.04799
0.18819
0.05036
0.08457
0.03376
0.05227
0.0738
0.05069
0.1288
0.13839
0.05439
0.09012
0.03844
0.00024
0.18833
0.09387
0.16621
0.12467
0.12854
0.18341
0.14421
0.03356
0.07983
0.15107
0.01253
0.08695
0.1013
0.19489
0.15074
0.15311
0.00288
0.16232
0.08599
0.13719
0.1926
0.14374
0.12144
0.01973
0.16262
0.17559
0.04586
0.02808
0.09565
0.1281
0.12589
0.16155
0.11897
0.00186
0.14365
0.0203
0.15368
0.19238
0.105
0.00056
0.02432
0.17691
0.18947
0.10196
0.1389
0.03061
0.01165
0.01036
0.162
0.01191
0.02758
0.00182
0.05864
0.04451
0.05976
0.18652
0.15265
0.1707
0.164
0.13132
0.19382
0.12173
0.02596
0.0383
0.00521
0.04763
0.00568
0.04203
0.18318
0.10541
0.07804
0.14375
0.04503
0.11704
0.03997
0.08113
0.14728
0.01926
0.01052
0.07806
0.14783
0.0149
0.00458
0.11316
0.0949
0.17771
0.13532
0.02534
0.05287
0.07849
0.12215
0.16352
0.0995
0.15311
0.08606
0.1302
0.1035
0.08642
0.07609
0.01848
0.17747
0.1001
0.04434
0.08487
0.03406
0.10189
0.1149
0.08105
0.05515
0.11933
0.02274
0.16356
0.05332
0.00037
0.18795
0.03212
0.14138
0.0686
0.14785
0.07759
0.13664
0.11699
0.15696
0.03175
0.04538
0.11867
0.1021
0.14298
0.16792
0.06609
0.12508
0.06705
0.18006
0.16797
0.13527
0.16336
0.02745
0.01518
0.03768
0.07726
0.06561
0.03155
0.11591
0.19612
0.17046
0.00254
0.13211
0.16988
0.10758
0.17171
0.06102
0.16592
0.09592
0.1847
0.0245
0.10216
0.13203
0.13906
0.04788
0.00508
0.1724
0.10679
0.00838
0.00831
0.13808
0.03057
0.15667
0.08896
0.02912
0.08403
0.05582
0.04448
0.18776
0.17285
0.14939
0.14649
0.07919
0.00386
0.09024
0.15563
0.00064
0.04327
0.17072
0.18566
0.00723
0.00703
0.11312
0.13129
0.0594
0.11965
0.15756
0.16477
0.14293
0.15942
0.15803
0.13358
0.15828
0.16659
0.13277
0.1966
0.11156
0.06411
0.06433
0.01817
0.08942
0.13317
0.16341
0.05985
0.10409
0.0191
0.19933
0.14927
0.05961
0.17446
0.10311
0.16152
0.03186
0.00577
0.05482
0.12643
0.13555
0.15419
0.03975
0.08039
0.10913
0.10821
0.16767
0.05335
0.12391
0.04774
0.03688
0.14044
0.03633
0.07865
0.0709
0.00305
0.07703
0.13695
0.11044
0.04799
0.12715
0.14483
0.14215
0.04549
0.0993
0.10337
0.16057
0.16432
0.01293
0.19542
0.1473
0.01718
0.02882
0.0891
0.01527
0.18728
0.03418
0.08565
0.13336
0.14814
0.11282
0.11916
0.0131
0.14767
0.16743
0.08816
0.14648
0.17163
0.18562
0.18578
0.04412
0.1973
0.12009
0.10683
0.12441
0.03199
0.19836
0.02409
0.10969
0.18411
0.09062
0.18863
0.06721
0.18419
0.11651
0.00053
0.16715
0.06179
0.08911
0.0574
0.17013
0.11958
0.16284
0.06092
0.04254
0.05475
0.05501
0.1805
0.11257
0.04211
0.16028
0.09315
0.03634
0.05908
0.18198
0.05818
0.18071
0.06048
0.08561
0.08559
0.17718
0.0641
0.08735
0.06297
0.18895
0.10543
0.0172
0.11542
0.04171
0.05632
0.19566
0.13128
0.10945
0.03825
0.17798
0.13672
0.08894
0.15491
0.02684
0.07531
0.05611
0.17315
0.06549
0.06932
0.18866
0.11568
0.18469
0.02423
0.03765
0.14085
0.05127
0.04386
0.10489
0.12649
0.11351
0.04013
0.05781
0.18994
1e-05
0.0271
0.11316
0.16063
0.09923
0.01847
0.04444
0.13678
0.03974
0.18355
0.11662
0.16411
0.06326
0.13417
0.04814
0.08438
0.01686
0.10798
0.03569
0.18164
0.00888
0.10126
0.10644
0.06201
0.11422
0.14992
0.02876
0.09611
0.12161
0.01659
0.12335
0.0949
0.19592
0.10057
0.00258
0.12093
0.13773
0.16222
0.02237
0.09707
0.12608
0.10295
0.09108
0.10729
0.11087
0.03632
0.1071
0.04191
0.02625
0.04441
0.16791
0.14454
0.01027
0.046
0.07398
0.07481
0.14987
0.14895
0.15346
0.01419
0.07958
0.09668
0.18211
0.15336
0.09306
0.00106
0.17534
0.19712
0.06882
0.13782
0.13898
0.14061
0.07097
0.06407
0.126
0.03629
0.05095
0.10005
0.11395
0.08947
0.00977
0.08354
0.02498
0.16277
0.11494
0.00684
0.15481
0.15841
0.10817
0.08552
0.00645
0.08495
0.04551
0.07059
0.09345
0.09911
0.02396
0.19407
0.05626
0.03746
0.06503
0.05334
0.07532
0.11184
0.16843
0.00837
0.03402
0.01002
0.00411
0.07717
0.14706
0.00423
0.09607
0.05634
0.17354
0.04827
0.06653
0.08004
0.11128
0.07719
0.17932
0.12051
0.1006
0.00201
0.13248
0.11037
0.01172
0.15722
0.10046
0.06512
0.11827
0.14351
0.00254
0.10873
0.18414
0.08855
0.04275
0.00762
0.01129
0.14684
0.14618
0.17072
0.10862
0.09413
0.02392
0.04456
0.14651
0.07928
0.05263
0.09554
0.1944
0.11209
0.13311
0.02767
0.10133
0.11969
0.08298
0.17826
0.10623
0.15961
0.18221
0.00438
0.18133
0.15986
0.0915
0.0332
0.15814
0.02996
0.18838
0.17018
0.19471
0.06094
0.04939
0.07561
0.00082
0.19995
0.06932
0.16254
0.12051
0.1075
0.13484
0.13259
0.14868
0.09229
0.18539
0.03642
0.06732
0.12175
0.04593
0.17008
0.11074
0.09788
0.05407
0.0845
0.06385
0.15037
0.18257
0.0246
0.07649
0.1083
0.05213
0.10577
0.18927
0.10552
0.1072
0.05655
0.02416
0.05475
0.07531
0.05738
0.18603
0.19085
0.13975
0.08318
0.0958
0.1091
0.00578
0.08297
0.14078
0.09225
0.10839
0.13139
0.06562
0.01623
0.02054
0.12092
0.10273
0.10475
0.05965
0.17902
0.00038
0.06839
0.14507
0.17573
0.16948
0.10483
0.19176
0.1512
0.02249
0.15259
0.0303
0.15038
0.12609
0.07808
0.11124
0.17182
0.18489
0.06747
0.00796
0.13805
0.00494
0.00635
0.04629
0.07135
0.04106
0.02052
0.02717
0.14256
0.19206
0.10839
0.11977
0.04766
0.05179
0.13619
0.13325
0.01664
0.02116
0.12941
0.15314
0.11054
0.03594
0.00698
0.19535
0.05076
0.10041
0.0424
0.14376
0.14261
0.05754
0.13522
0.13019
0.04903
0.05297
0.13138
0.13548
0.0692
0.08178
0.06579
0.06185
0.05955
0.17116
0.07593
0.04079
0.07169
0.06214
0.19952
0.03665
0.18169
0.03557
0.17922
0.14503
0.12113
0.00695
0.13688
0.00825
0.14833
0.03849
0.0972
0.18363
0.01461
0.08083
0.05086
0.14475
0.04161
0.17576
0.06537
0.07111
0.05402
0.00345
0.1367
0.09906
0.10104
0.07029
0.10773
0.15166
0.16161
0.15719
0.06964
0.19698
0.18316
0.14557
0.02935
0.0745
0.0085
0.16147
0.08637
0.13229
0.01066
0.18905
0.18278
0.05244
0.06335
0.02708
0.08767
0.17701
0.0863
0.10637
0.14395
0.01689
0.05298
0.175
0.06038
0.03206
0.13785
0.06462
0.00817
0.1787
0.14402
0.16058
0.11761
0.10147
0.17354
0.09114
0.11472
0.18475
0.06456
0.13455
0.15852
0.11336
0.13247
0.06074
0.07165
0.14258
0.09144
0.09344
0.06547
0.14835
0.17692
0.05045
0.10326
0.07553
0.10503
0.18646
0.02371
0.06739
0.01425
0.10234
0.0861
0.1969
0.08516
0.09354
0.02813
0.1675
0.03051
0.14549
0.16033
0.15808
0.08135
0.14054
0.1025
0.07233
0.0757
0.15169
0.0937
0.10787
0.10926
0.01161
0.13647
0.12313
0.12264
0.18979
0.05277
0.13669
0.16947
0.14188
0.10379
0.06993
0.06807
0.19802
0.10523
0.07092
0.08386
0.07492
0.05176
0.1821
0.17077
0.06826
0.10141
0.08145
0.05137
0.00545
0.15614
0.00759
0.1366
0.17192
0.06719
0.1393
0.12067
0.00768
0.1904
0.13786
0.17537
0.00344
0.03256
0.15677
0.11047
0.18639
0.06305
0.07555
0.11941
0.12285
0.04548
0.10988
0.18666
0.15312
0.06187
0.05145
0.19728
0.14316
0.0769
0.18621
0.10917
0.03961
0.05016
0.1186
0.12287
0.13924
0.05015
0.08353
0.12602
0.00011
0.16211
0.14039
0.14144
0.09567
0.1493
0.03744
0.06717
0.11984
0.09758
0.09983
0.03977
0.14314
0.16448
0.18008
0.03336
0.09503
0.06755
0.184
0.18011
0.17563
0.15456
0.14531
0.08018
0.14974
0.12278
0.04587
0.031
0.11831
0.07141""".split("\n")
processed_data_1 = []
for i in raw_data_1:
    processed_data_1.append(float(i))
    


raw_data_2 = """4.97707
5.39853
5.49943
5.6012
5.59793
5.70362
6.32491
6.43104
6.63741
6.42406
6.63
6.52322
7.24933
7.3524
7.56052
7.66773
7.7743
13.0103
7.778
7.98459
8.09181
8.09486
8.09333
8.30515
8.41062
8.72247
9.45598
9.55906
9.24329
9.35313
9.35487
9.35661
9.67456
10.0901
10.0921
10.1991
10.1958
10.3022
10.4044
10.719
11.0296
11.4504
11.9732
12.4905
12.4936
12.4892
13.112
13.2064
13.4104
13.4132
13.6178
13.6204
13.8248
13.8174
13.7194
13.8211
18.7577
14.2326
13.8122
14.1356
14.4533
15.0818
15.0866
15.0844
15.1971
15.298
15.8258
16.4551
16.7692
16.772
16.77
17.2952
17.5049
17.9213
19.1778
20.2112
19.9959
19.9992
20.1994
20.1933
20.4062
20.5028
20.9155
21.016
21.1352
21.661
23.5548
22.1856
22.7127
23.0313
23.0283
23.3475
24.1859
25.3378
25.8566
26.27
27.0859
27.0798
27.2858
27.5922
27.5871
27.5828
27.6811
27.9877
27.9907
27.904
27.9088
28.1213
28.7513
29.7114
28.867
28.969
28.9744
29.2911
29.5033
29.5044
33.3642
30.3467
30.3412
30.8616
31.075
31.8089
32.5379
32.9528
33.0537
33.3609
33.8785
34.0807
33.7508
34.0574
34.1574
34.4682
34.7844
34.7983
35.2207
35.0187
35.0248
35.3335
35.3425
35.6504
35.7583
36.3913
36.4911
37.5424
37.8416
38.785
39.3121
39.6303
39.9487
40.5699
41.2
41.3078
41.9285
41.9319
42.4478
43.2739
43.5733
43.8873
44.8168
45.6588
45.8767
45.9733
46.2971
46.7212
46.8312
47.2472
47.7726
48.5092
49.0266
""".split("\n")
processed_data_2 = []
for i in raw_data_2:
    processed_data_2.append(float(i))
