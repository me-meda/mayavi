# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.image_decompose_filter import ImageDecomposeFilter


class ImageFourierFilter(ImageDecomposeFilter):
    """
    ImageFourierFilter - Superclass that implements complex numbers.
    
    Superclass: ImageDecomposeFilter
    
    ImageFourierFilter is a class of filters that use complex numbers
    this superclass is a container for methods that manipulate these
    structure including fast Fourier transforms.  Complex numbers may
    become a class. This should really be a helper class.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageFourierFilter, obj, update, **traits)
    
    def execute_fft(self, *args):
        """
        V.execute_fft(ImageComplex, ImageComplex, int)
        C++: void ExecuteFft(ImageComplex *in, ImageComplex *out,
            int N)
        This function calculates the whole fft of an array. The contents
        of the input array are changed. (It is engineered for no
        decimation)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ExecuteFft, *my_args)
        return ret

    def execute_rfft(self, *args):
        """
        V.execute_rfft(ImageComplex, ImageComplex, int)
        C++: void ExecuteRfft(ImageComplex *in, ImageComplex *out,
            int N)
        This function calculates the whole fft of an array. The contents
        of the input array are changed. (It is engineered for no
        decimation)
        """
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.ExecuteRfft, *my_args)
        return ret

    _updateable_traits_ = \
    (('dimensionality', 'GetDimensionality'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('progress_text', 'GetProgressText'),
    ('debug', 'GetDebug'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'debug', 'global_warning_display',
    'release_data_flag', 'dimensionality', 'number_of_threads',
    'progress_text'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageFourierFilter, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageFourierFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['dimensionality', 'number_of_threads']),
            title='Edit ImageFourierFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageFourierFilter properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

