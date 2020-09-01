class Split():
  """
  Split contains a full split lss file all parsed into concice and usable data structures

  Variables
  ---------
  game_name : str
    Contains the name of the game that the splits were used for.

  category_name : str
    Contains the name of the category the user ran 

  attempt_count : str
    Contains the number of attempts the user has attempted on the split file

  attempts : list
    Contains Attempt objects that describe each of the attempts a user has preformed 

  best_segments : list
    Contains Segment objects that are the best the user has preformed

  pb_segments : list
    Contains Segment objects that hold the pb of the user.
  """
  def __init__(self):
    self.game_name = None
    self.category_name = None
    self.attempt_count = None
    self.attempts = []
    self.best_segments = []
    self.pb_segments = []

class Attempt():
  """
    Attempt contains all of the information about each attempt a user has performed 

    Variables
    ---------
    did_complete : bool 
      Contains a boolean that keeps track if the run finished or not.

    date_start : str
      Contains the date of when the run started in MM/DD/YYYY format

    date_end : str
      Contains the date of when the run ended in MM/DD/YYYY format

    ltime_start : str
      Contains the time of day the user started the run in the format HH:MM:SS

    ltime_end : str
      Contains the time of day the user ended the run in the format HH:MM:SS

    rtime : str
      If the user completed the run, this will contain the real time completion time. Otherwise, will be None
    
    gtime : str
      If the user completed the run, this will contain the game time completion time. Otherwise, will be None

    segments : list
      Contains Segment objects that hold each segment for this current attempt.
  """
  def __init__(self):
    self.did_complete = False
    self.date_start = None
    self.date_end = None
    self.ltime_start = None
    self.ltime_end = None
    self.rtime = None
    self.gtime = None
    self.segments = []
    
class Segment():
  """
    Contains each Segment for an attempt

    Variables
    ---------
    real_time : str 
      Contains the real time for the segment

    game_time : str
      Contains the game time for the segment

    seg_name : str
      Contains the name of the segment
  """
  def __init__(self):
    self.real_time = None
    self.game_time = None
    self.seg_name = None