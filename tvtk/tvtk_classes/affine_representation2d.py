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

from tvtk.tvtk_classes.affine_representation import AffineRepresentation


class AffineRepresentation2D(AffineRepresentation):
    """
    AffineRepresentation2D - represent 2d affine transformations
    
    Superclass: AffineRepresentation
    
    This class is used to represent a AffineWidget. This
    representation consists of three parts: a box, a circle, and a cross.
    The box is used for scaling and shearing, the circle for rotation,
    and the cross for translation. These parts are drawn in the overlay
    plane and maintain a constant size (width and height) specified in
    terms of normalized viewport coordinates.
    
    The representation maintains an internal transformation matrix (see
    superclass' get_transform() method). The transformations generated by
    this widget assume that the representation lies in the x-y plane. If
    this is not the case, the user is responsible for transforming this
    representation's matrix into the correct coordinate space (by
    judicious matrix multiplication). Note that the transformation matrix
    returned by get_transform() is relative to the last place_widget()
    invocation. (The place_widget() sets the origin around which rotation
    and scaling occurs; the origin is the center point of the bounding
    box provided.)
    
    See Also:
    
    AffineRepresentation AffineWidget
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkAffineRepresentation2D, obj, update, **traits)
    
    display_text = tvtk_base.true_bool_trait(help=\
        """
        Enable the display of text with numeric values characterizing the
        transformation. Rotation and shear are expressed in degrees;
        translation the distance in world coordinates; and scale
        normalized (sx,sy) values.
        """
    )
    def _display_text_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetDisplayText,
                        self.display_text_)

    origin = traits.Array(shape=(3,), value=(0.0, 0.0, 0.0), dtype=float, enter_set=True, auto_set=False, cols=3, help=\
        """
        Specify the origin of the widget (in world coordinates). The
        origin is the point where the widget places itself. Note that
        rotations and scaling occurs around the origin.
        """
    )
    def _origin_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOrigin,
                        self.origin)

    box_width = traits.Trait(100, traits.Range(10, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the width of the various parts of the representation (in
        pixels).  The three parts are of the representation are the
        translation axes, the rotation circle, and the scale/shear box.
        Note that since the widget resizes itself so that the width and
        height are always the same, only the width needs to be specified.
        """
    )
    def _box_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetBoxWidth,
                        self.box_width)

    circle_width = traits.Trait(75, traits.Range(10, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the width of the various parts of the representation (in
        pixels).  The three parts are of the representation are the
        translation axes, the rotation circle, and the scale/shear box.
        Note that since the widget resizes itself so that the width and
        height are always the same, only the width needs to be specified.
        """
    )
    def _circle_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetCircleWidth,
                        self.circle_width)

    def _get_selected_property(self):
        return wrap_vtk(self._vtk_obj.GetSelectedProperty())
    def _set_selected_property(self, arg):
        old_val = self._get_selected_property()
        self._wrap_call(self._vtk_obj.SetSelectedProperty,
                        deref_vtk(arg))
        self.trait_property_changed('selected_property', old_val, arg)
    selected_property = traits.Property(_get_selected_property, _set_selected_property, help=\
        """
        Set/Get the properties when unselected and selected.
        """
    )

    def _get_text_property(self):
        return wrap_vtk(self._vtk_obj.GetTextProperty())
    def _set_text_property(self, arg):
        old_val = self._get_text_property()
        self._wrap_call(self._vtk_obj.SetTextProperty,
                        deref_vtk(arg))
        self.trait_property_changed('text_property', old_val, arg)
    text_property = traits.Property(_get_text_property, _set_text_property, help=\
        """
        Set/Get the properties when unselected and selected.
        """
    )

    axes_width = traits.Trait(59, traits.Range(10, 2147483647, enter_set=True, auto_set=False), help=\
        """
        Specify the width of the various parts of the representation (in
        pixels).  The three parts are of the representation are the
        translation axes, the rotation circle, and the scale/shear box.
        Note that since the widget resizes itself so that the width and
        height are always the same, only the width needs to be specified.
        """
    )
    def _axes_width_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetAxesWidth,
                        self.axes_width)

    def _get_property(self):
        return wrap_vtk(self._vtk_obj.GetProperty())
    def _set_property(self, arg):
        old_val = self._get_property()
        self._wrap_call(self._vtk_obj.SetProperty,
                        deref_vtk(arg))
        self.trait_property_changed('property', old_val, arg)
    property = traits.Property(_get_property, _set_property, help=\
        """
        Set/Get the properties when unselected and selected.
        """
    )

    def place_widget(self, *args):
        """
        V.place_widget([float, float, float, float, float, float])
        C++: virtual void PlaceWidget(double bounds[6])
        Subclasses of AffineRepresentation2D must implement these
        methods. These are the methods that the widget and its
        representation use to communicate with each other. Note:
        place_widget() reinitializes the transformation matrix (i.e., sets
        it to identity). It also sets the origin for scaling and
        rotation.
        """
        ret = self._wrap_call(self._vtk_obj.PlaceWidget, *args)
        return ret

    _updateable_traits_ = \
    (('origin', 'GetOrigin'), ('display_text', 'GetDisplayText'),
    ('allocated_render_time', 'GetAllocatedRenderTime'), ('handle_size',
    'GetHandleSize'), ('estimated_render_time', 'GetEstimatedRenderTime'),
    ('need_to_render', 'GetNeedToRender'), ('dragable', 'GetDragable'),
    ('axes_width', 'GetAxesWidth'), ('visibility', 'GetVisibility'),
    ('render_time_multiplier', 'GetRenderTimeMultiplier'), ('box_width',
    'GetBoxWidth'), ('circle_width', 'GetCircleWidth'),
    ('reference_count', 'GetReferenceCount'), ('place_factor',
    'GetPlaceFactor'), ('pickable', 'GetPickable'), ('tolerance',
    'GetTolerance'), ('use_bounds', 'GetUseBounds'), ('debug',
    'GetDebug'), ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'display_text', 'dragable', 'global_warning_display',
    'need_to_render', 'pickable', 'use_bounds', 'visibility',
    'allocated_render_time', 'axes_width', 'box_width', 'circle_width',
    'estimated_render_time', 'handle_size', 'origin', 'place_factor',
    'render_time_multiplier', 'tolerance'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(AffineRepresentation2D, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit AffineRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['display_text', 'need_to_render', 'use_bounds',
            'visibility'], [], ['allocated_render_time', 'axes_width',
            'box_width', 'circle_width', 'estimated_render_time', 'handle_size',
            'origin', 'place_factor', 'render_time_multiplier', 'tolerance']),
            title='Edit AffineRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit AffineRepresentation2D properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

