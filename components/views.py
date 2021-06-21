from django.shortcuts import render
from django.views import View

#UI-ELEMENTS
class AlertsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Alerts"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-alerts.html',greeting)

class ButtonsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Buttons"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-buttons.html',greeting)

class CardsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Cards"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-cards.html',greeting)    

class CarouselView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Carousel"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-carousel.html',greeting)  


class DropDownsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Dropdowns"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-dropdwons.html',greeting)                    

class GridView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Grid"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-grid.html',greeting) 

class ImagesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Images"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-images.html',greeting)   

class LightBoxView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Lightbox"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-lightbox.html',greeting)    

class ModalsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Modals"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-modals.html',greeting) 

class RangeSlidebarView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Range Slider"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-rangeslidebar.html',greeting) 

class SessionTimeoutView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Session Timeout"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-sessiontimeout.html',greeting)           

class ProgressBarsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Progress Bars"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-progressbars.html',greeting)    

class SweetAlertView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Sweet-Alert"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-sweetalert.html',greeting)     

class TabsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Tabs & Accordions"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-tabs.html',greeting)   

class TypoGraphyView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Typography"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-typography.html',greeting)   

class VideoView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Video"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-video.html',greeting)   


class GeneralView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "General"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-general.html',greeting)                                                                           

class ColorsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Colors"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-colors.html',greeting)  

class RatingView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Rating"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-rating.html',greeting)  


class NotificationsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Notifications"
        greeting['pageview'] = "UI Elements"
        return render (request,'components/ui-elements/components-notifications.html',greeting)

##FORMS
class FormelementsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Elements"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formelements.html',greeting)


class FormLayoutsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Layouts"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formlayouts.html',greeting)

        
class FormValidationView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Validation"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formvalidation.html',greeting)        

        
class FormAdvancedView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Advanced"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formadvanced.html',greeting)           


class FormEditorsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Editors"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formeditors.html',greeting)         

        
class FormFileuploadView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form File Upload"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formfileupload.html',greeting) 

class FormXeditableView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Xeditable"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formxeditable.html',greeting) 
              
class FormRepeaterView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Repeater"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrepeater.html',greeting) 
           

class FormWizardView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Wizard"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrwizard.html',greeting)                  
        
class FormMaskView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Form Mask"
        greeting['pageview'] = "Forms"
        return render (request,'components/forms/components-formrmask.html',greeting)         

        
##Tables
class BasicTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Basic Tables"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-basictables.html',greeting)  

class DataTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Data Tables"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-datatables.html',greeting) 


class ResponsiveTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Responsive Table"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-responsivetables.html',greeting) 

class EditableTablesView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Editable Table"
        greeting['pageview'] = "Tables"
        return render (request,'components/tables/components-editabletables.html',greeting) 

#Charts     
class ApexChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Apex Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-apexcharts.html',greeting)  

class EChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "E Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-echarts.html',greeting)  

class ChartJsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Chartjs Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-chartjs.html',greeting)  

class FlotChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Flot Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-flotcharts.html',greeting)    


class ToastUiChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Toast UI Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-toastuicharts.html',greeting)                  
                         

class JqueryKnobChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Jquery Knob Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-jqueryknobcharts.html',greeting)   

class SparklineChartsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Sparkline Charts"
        greeting['pageview'] = "Charts"
        return render (request,'components/charts/components-sparklinecharts.html',greeting)                                   

#Icons        
class BoxIconsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Boxicons"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-boxicons.html',greeting)         
        

class MaterialDesignView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Material Design"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-materialdesign.html',greeting)    


class DripIconsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Dripicons"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-dripicons.html',greeting)  

class FontAwesomeView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Font Awesome"
        greeting['pageview'] = "Icons"
        return render (request,'components/icons/components-fontawesome.html',greeting)                     

#Maps
class GoogleMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Google Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-googlemaps.html',greeting) 

class VectorMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Vector Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-vectormaps.html',greeting)      

class LeafletMapsView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Leaflet Maps"
        greeting['pageview'] = "Maps"
        return render (request,'components/maps/components-leafletmaps.html',greeting)            
        