class Transect(object):
    
    def __init__(self, native_cover, plant_community, native_indicators):
        self.native_cover = native_cover
        self.plant_community = plant_community
        self.native_indicators = native_indicators
        
    def __repr__(self):
        return f'Transect({self.native_cover!r},{self.plant_community!r}, {self.native_indicators!r})'
    
    def __str__(self):
        return "{} {} {}".format(self.native_cover, self.plant_community, self.native_indicators)

    @property
    def state(self):
        if self.native_cover=='N0' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '1'
        elif self.native_cover=='N0' and self.plant_community=='Shrub' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '2'
        elif self.native_cover=='N0' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '3'
        elif self.native_cover=='N0' and self.plant_community=='Herb' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '4'
        elif self.native_cover=='N25' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '5'
        elif self.native_cover=='N25' and self.plant_community=='Shrub' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '6'
        elif self.native_cover=='N25' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '7'
        elif self.native_cover=='N25' and self.plant_community=='Herb' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '8'
        elif self.native_cover=='N50' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '9'
        elif self.native_cover=='N50' and self.plant_community=='Shrub' and self.native_indicators=='I1':
            return '10'
        elif self.native_cover=='N50' and self.plant_community=='Shrub' and self.native_indicators=='I2':
            return '11'
        elif self.native_cover=='N50' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '12'
        elif self.native_cover=='N50' and self.plant_community=='Herb' and self.native_indicators=='I1':
            return '13'
        elif self.native_cover=='N50' and self.plant_community=='Herb' and self.native_indicators=='I2':
            return '14'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '15'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and self.native_indicators=='I1':
            return '16'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and self.native_indicators=='I2':
            return '17'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '18'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and self.native_indicators=='I1':
            return '19'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and self.native_indicators=='I2':
            return '20'
        
    @property
    def state_daren(self):
        if self.native_cover=='N0' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '1'
        elif self.native_cover=='N0' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '2'
        elif self.native_cover=='N0' and self.plant_community=='Shrub' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '3'
        elif self.native_cover=='N0' and self.plant_community=='Herb' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '4'
        elif self.native_cover=='N25' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '5'
        elif self.native_cover=='N25' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '6'
        elif self.native_cover=='N25' and self.plant_community=='Shrub' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '7'
        elif self.native_cover=='N25' and self.plant_community=='Herb' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '8'
        elif self.native_cover=='N50' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '9'
        elif self.native_cover=='N50' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '10'
        elif self.native_cover=='N50' and self.plant_community=='Shrub' and self.native_indicators=='I1':
            return '11'
        elif self.native_cover=='N50' and self.plant_community=='Herb' and self.native_indicators=='I1':
            return '12'
        elif self.native_cover=='N50' and self.plant_community=='Shrub' and self.native_indicators=='I2':
            return '13'
        elif self.native_cover=='N50' and self.plant_community=='Herb' and self.native_indicators=='I2':
            return '14'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '15'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '16'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and self.native_indicators=='I1':
            return '17'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and self.native_indicators=='I1':
            return '18'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and self.native_indicators=='I2':
            return '19'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and self.native_indicators=='I2':
            return '20'
        
    @property
    def state_condensed(self):
        if self.native_cover=='N0' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '1'
        elif self.native_cover=='N0' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '2'
        elif self.native_cover=='N0' and self.plant_community=='Herb' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '3'
        elif self.native_cover=='N0' and self.plant_community=='Shrub' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '4'
        elif (self.native_cover=='N25' or self.native_cover=='N50') and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '5'
        elif (self.native_cover=='N25' or self.native_cover=='N50') and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '6'
        elif (self.native_cover=='N25' or self.native_cover=='N50') and self.plant_community=='Shrub' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '7'
        elif (self.native_cover=='N25' or self.native_cover=='N50') and self.plant_community=='Herb' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '8'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and self.native_indicators=='I0':
            return '9'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and self.native_indicators=='I0':
            return '10'
        elif self.native_cover=='N75' and self.plant_community=='Shrub' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '11'
        elif self.native_cover=='N75' and self.plant_community=='Herb' and (self.native_indicators=='I1' or self.native_indicators=='I2'):
            return '12'