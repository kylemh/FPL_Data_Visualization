<h4>Please view using NBVIEWER by clicking here:
<br>
http://nbviewer.jupyter.org/github/kylemh/FPL-DataVisualization/blob/master/jupyter_viz.ipynb</h4>

```python
import pandas as pd
import matplotlib.pyplot as plt
player_data = pd.read_csv('/Users/zoeolson1/player_data.csv')
player_data.head(2)
```

    /Users/zoeolson1/anaconda/lib/python2.7/site-packages/matplotlib/font_manager.py:273: UserWarning: Matplotlib is building the font cache using fc-list. This may take a moment.
      warnings.warn('Matplotlib is building the font cache using fc-list. This may take a moment.')

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>dob</th>
      <th>name</th>
      <th>nationality</th>
      <th>height</th>
      <th>weight</th>
      <th>wins</th>
      <th>fouls</th>
      <th>pl_goals</th>
      <th>losses</th>
      <th>...</th>
      <th>last_man_tackle</th>
      <th>clearance_off_line</th>
      <th>saves</th>
      <th>punches</th>
      <th>goal_kicks</th>
      <th>penalty_save</th>
      <th>keeper_throws</th>
      <th>good_high_claim</th>
      <th>total_keeper_sweeper</th>
      <th>stand_catch_dive_catch</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3452</td>
      <td>11/26/90</td>
      <td>Danny Welbeck</td>
      <td>England</td>
      <td>185cm</td>
      <td>73kg</td>
      <td>87</td>
      <td>89</td>
      <td>34</td>
      <td>35</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5001</td>
      <td>12/1/94</td>
      <td>Emre Can</td>
      <td>Germany</td>
      <td>184cm</td>
      <td>82kg</td>
      <td>29</td>
      <td>68</td>
      <td>2</td>
      <td>16</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 56 columns</p>
</div>



We are going to look at how players score goals, and weather goals are more frequently made with the left foot, right foot, or head. First, we will clean our data by replacing all of the NaN values with '0', because this is how they appear in the original CSV. Below we have a list of all of the head, left foot, and right foot goals of each player. 


```python
df = pd.DataFrame(player_data, columns = ['att_hd_goal', 'att_lf_goal', 'att_rf_goal'])
df2 = df.fillna(0)
df2.head(2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>att_hd_goal</th>
      <th>att_lf_goal</th>
      <th>att_rf_goal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



Now, we will format the dataframe to make it suitable for a pie chart. We will do so by aggregating each column to get the total head, right foot, and left foot goals. Then creating leables for each of these categories. 


```python
df2.columns = ['header', 'left-foot', 'right-foot']
df2.loc['Total']= df2.sum()
df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>header</th>
      <th>left-foot</th>
      <th>right-foot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>18.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.0</td>
      <td>6.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>2.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.0</td>
      <td>5.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>3.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1.0</td>
      <td>6.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>3.0</td>
      <td>2.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>7.0</td>
      <td>2.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.0</td>
      <td>19.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>4.0</td>
      <td>4.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>538</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>539</th>
      <td>3.0</td>
      <td>0.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>540</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>541</th>
      <td>1.0</td>
      <td>18.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>542</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>543</th>
      <td>2.0</td>
      <td>12.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>544</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>545</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>546</th>
      <td>0.0</td>
      <td>2.0</td>
      <td>14.0</td>
    </tr>
    <tr>
      <th>547</th>
      <td>0.0</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>548</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>549</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>550</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>551</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>552</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>553</th>
      <td>0.0</td>
      <td>3.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>554</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>555</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>556</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>557</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>558</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>559</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>560</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>17.0</td>
    </tr>
    <tr>
      <th>561</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>562</th>
      <td>3.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>563</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>564</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>565</th>
      <td>3.0</td>
      <td>5.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>566</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>Total</th>
      <td>655.0</td>
      <td>1048.0</td>
      <td>2067.0</td>
    </tr>
  </tbody>
</table>
<p>568 rows × 3 columns</p>
</div>



Great, we have a total row. Now lets remove all of the data except for the column headers and totals. 


```python
goal_types = df2.T
```


```python
goal_types.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>558</th>
      <th>559</th>
      <th>560</th>
      <th>561</th>
      <th>562</th>
      <th>563</th>
      <th>564</th>
      <th>565</th>
      <th>566</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>header</th>
      <td>9.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>655.0</td>
    </tr>
    <tr>
      <th>left-foot</th>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>1048.0</td>
    </tr>
    <tr>
      <th>right-foot</th>
      <td>18.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>17.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>2067.0</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 568 columns</p>
</div>




```python
goal_types = pd.DataFrame(goal_types['Total'])

goal_types.head(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>header</th>
      <td>655.0</td>
    </tr>
    <tr>
      <th>left-foot</th>
      <td>1048.0</td>
    </tr>
    <tr>
      <th>right-foot</th>
      <td>2067.0</td>
    </tr>
  </tbody>
</table>
</div>



Great, now our data frame is ready for a pie chart display!  
For our pie chart, we will choose colors using iWantHue ( http://tools.medialab.sciences-po.fr/iwanthue/ ).



```python
colors = ["#e49300", "#0263f3", "#dbff62", "#ff004e","#a14400"]

plt.pie(goal_types['Total'], labels = goal_types.index, shadow= False, colors = colors, explode = (0, 0, 0), startangle = 90, autopct='%1.1f%%',)

plt.axis('equal')

plt.tight_layout()
plt.show()
```


![png](jupyter_viz_files/jupyter_viz_10_0.png)


Yay! We have our pie chart. Now lets look at what other factors go into goal scoring..


```python
ng = pd.DataFrame(player_data, columns = ['nationality', 'id', 'pl_goals', 'appearances', 'blocked_scoring_att'])
nat_goals = ng.fillna(0)
nat_goals.head(3)

```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nationality</th>
      <th>id</th>
      <th>pl_goals</th>
      <th>appearances</th>
      <th>blocked_scoring_att</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>England</td>
      <td>3452</td>
      <td>34</td>
      <td>154</td>
      <td>84.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Germany</td>
      <td>5001</td>
      <td>2</td>
      <td>60</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spain</td>
      <td>4805</td>
      <td>10</td>
      <td>39</td>
      <td>13.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
nat_goals2 = (nat_goals.groupby(['nationality'],as_index=False).id.count())
nat_goals2.head()


```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nationality</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Algeria</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Argentina</td>
      <td>16</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Armenia</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Australia</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
nat_goals3 = (nat_goals.groupby(['nationality'],as_index=False).pl_goals.sum())
nat_goals3.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nationality</th>
      <th>pl_goals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Algeria</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Argentina</td>
      <td>152</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Armenia</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Australia</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
merged_goals = pd.merge(left=nat_goals2,right=nat_goals3, left_on='nationality', right_on='nationality')
merged_goals
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nationality</th>
      <th>id</th>
      <th>pl_goals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Algeria</td>
      <td>4</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Argentina</td>
      <td>16</td>
      <td>152</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Armenia</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Australia</td>
      <td>5</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Austria</td>
      <td>7</td>
      <td>23</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Belgium</td>
      <td>23</td>
      <td>289</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bosnia And Herzegovina</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Brazil</td>
      <td>12</td>
      <td>96</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Cameroon</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Canada</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Chile</td>
      <td>2</td>
      <td>33</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Colombia</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Congo</td>
      <td>3</td>
      <td>20</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Costa Rica</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Cote D'Ivoire</td>
      <td>7</td>
      <td>107</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Croatia</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Curacao</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Czech Republic</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Denmark</td>
      <td>5</td>
      <td>23</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Ecuador</td>
      <td>4</td>
      <td>29</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Egypt</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>22</th>
      <td>England</td>
      <td>207</td>
      <td>1585</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Equatorial Guinea</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Estonia</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>France</td>
      <td>30</td>
      <td>208</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Gabon</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Gambia</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Germany</td>
      <td>12</td>
      <td>44</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Ghana</td>
      <td>3</td>
      <td>16</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Italy</td>
      <td>6</td>
      <td>17</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Jamaica</td>
      <td>2</td>
      <td>7</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Japan</td>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Kenya</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Lithuania</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Mali</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Morocco</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Netherlands</td>
      <td>18</td>
      <td>45</td>
    </tr>
    <tr>
      <th>41</th>
      <td>New Zealand</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Nigeria</td>
      <td>9</td>
      <td>66</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Northern Ireland</td>
      <td>7</td>
      <td>47</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Norway</td>
      <td>4</td>
      <td>9</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Poland</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Portugal</td>
      <td>5</td>
      <td>7</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Romania</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Scotland</td>
      <td>17</td>
      <td>133</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Senegal</td>
      <td>7</td>
      <td>68</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Serbia</td>
      <td>5</td>
      <td>47</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Slovakia</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>52</th>
      <td>South Africa</td>
      <td>1</td>
      <td>19</td>
    </tr>
    <tr>
      <th>53</th>
      <td>South Korea</td>
      <td>3</td>
      <td>28</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Spain</td>
      <td>41</td>
      <td>243</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Sweden</td>
      <td>5</td>
      <td>38</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Switzerland</td>
      <td>6</td>
      <td>9</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Tunisia</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Turkey</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>United States</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Uruguay</td>
      <td>5</td>
      <td>15</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Venezuela</td>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Wales</td>
      <td>13</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
<p>63 rows × 3 columns</p>
</div>



Excellent! Now lets look at nations with over 10 players.


```python
final_data = merged_goals.loc[merged_goals['id'] >= 10]
```


```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
merged_goals.plot.bar()
```




    <matplotlib.axes._subplots.AxesSubplot at 0x11ab1af10>




```python
import plotly.graph_objs as go
import plotly.plotly as py

py.sign_in('zoe1114', 'gqr5grvyef')

trace1 = go.Bar(
    x=final_data['nationality'],
    y=final_data['id'],
    name='Players',
    marker=dict(
        color='rgb(55, 83, 109)'
    )
)
trace2 = go.Bar(
    x=final_data['nationality'],
    y=final_data['pl_goals'],
    name='Goals',
    marker=dict(
        color='rgb(26, 118, 255)'
    )
)
data = [trace1, trace2]
layout = go.Layout(
    title='# of Players vs. Goals Made',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='Count',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='style-bar')
```

    High five! You successfuly sent some data to your account on plotly. View your plot in your browser at https://plot.ly/~zoe1114/0 or inside your plot.ly account where it is named 'style-bar'





<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~zoe1114/0.embed" height="525px" width="100%"></iframe>




```python
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import pandas as pd

nd = pd.read_csv('/Users/zoeolson1/player_data3.csv')
nd.head(2)
nd['nationality'] = str(nd['nationality'])


words =' '.join(nd['nationality'])
print "amount of players for analysis: ", (len(words.split(",")))

cloud = WordCloud(font_path='System/Library/Fonts/Noteworthy.ttc', stopwords=STOPWORDS,
                      background_color='white',
                      width=500, height=500).generate(words)

plt.imshow(cloud)
plt.axis("off")
plt.show()
plt.close()
```

    amount of players for analysis:  536



![png](jupyter_viz_files/jupyter_viz_20_1.png)



```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

py.sign_in('zoe1114', 'gqr5grvyef')

nd = pd.read_csv('/Users/zoeolson1/player_data3.csv', parse_dates = True)
nd['dob'] = pd.to_datetime(nd['dob'])
nd['year2'] = nd['dob'].dt.year

layout = go.Layout(title='Year Born vs. Number of Appearances')

# Create traces
trace0 = go.Scatter(
    x = nd['year2'],
    y = nd['appearances'],
    mode = 'lines+markers',
    name = 'lines+markers'
)
#trace1 = go.Scatter(
 #   x = nd['dob'],
#    y = nd['wins'],
   # mode = 'lines+markers',
#    name = 'lines+markers'
#)
#trace2 = go.Scatter(
#    x = random_x,
#    y = random_y2,
#    mode = 'markers',
#    name = 'markers'
#)
data = [trace0]

# Plot and embed in ipython notebook!
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='line-mode')
```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~zoe1114/2.embed" height="525px" width="100%"></iframe>




```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd


df = pd.read_csv('/Users/zoeolson1/player_data3.csv')

dt = pd.DataFrame({'count' : df.groupby(['nationality', 'Latitude', 'Longitude'])['id'].count()}).reset_index()

dt['text'] = dt['nationality'] + '<br>Count ' + (dt['count']).astype(str)
limits = [(0,1),(2,6),(7,12),(13,17),(18,24),(25,30)]
colors = ["rgb(0,116,217)","rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","rgb(0,255, 255)", "rgb(255,255,51)"]
cities = []
                                    
                                      
for i in range(len(limits)):
    lim = limits[i]
    df_sub = dt[lim[0]:lim[1]]
    city = dict(
        type = 'scattergeo',
        locationmode = 'Africa',
        lon = df_sub['Latitude'],
        lat = df_sub['Longitude'],
        text = df_sub['text'],
        marker = dict(
            size = df_sub['count']*20,
            color = colors[i],
            line = dict(width=0.5, color='rgb(40,40,40)'),
            sizemode = 'area'
        ),
        name = '{0} - {1}'.format(lim[0],lim[1]) )
    cities.append(city)
                                      
layout = dict(
        title = '2014 English Primer League Player Orgins<br>(Click legend to toggle traces)',
        showlegend = True,
        geo = dict(
            scope='Europe',
            projection=dict( type='Mercator' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )

fig = dict( data=cities, layout=layout )
py.iplot( fig, validate=False, filename='d3-bubble-map-populations' )

```




<iframe id="igraph" scrolling="no" style="border:none;" seamless="seamless" src="https://plot.ly/~zoe1114/4.embed" height="525px" width="100%"></iframe>
